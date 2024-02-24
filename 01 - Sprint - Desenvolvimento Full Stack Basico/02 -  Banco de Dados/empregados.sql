-- Criando tabela de empregados
CREATE TABLE public.empregados (
   	empregado_id serial PRIMARY KEY,
    nome character(20) NOT NULL,
    data_registro DATE NOT NULL DEFAULT CURRENT_DATE,
    sexo character(2),
    endereco character(20),
    supervisor_id INT,
    FOREIGN KEY (supervisor_id) REFERENCES empregados(empregado_id)
);

-- Validacao para que nenhum supervisionado seja supervisor
CREATE OR REPLACE FUNCTION validar_supervisao() 
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.supervisor_id IS NOT NULL AND NEW.empregado_id = NEW.supervisor_id THEN
        RAISE EXCEPTION 'Um supervisor não pode ser supervisionado por si mesmo.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_validar_supervisao
BEFORE INSERT OR UPDATE ON empregados
FOR EACH ROW EXECUTE FUNCTION validar_supervisao();

-- Inserindo dados na tabela
INSERT INTO public.empregados (nome, data_registro, sexo, endereco, supervisor_id) VALUES('Angelo', CURRENT_DATE, 'M', 'Rua 1', NULL);
INSERT INTO public.empregados (nome, data_registro, sexo, endereco, supervisor_id) VALUES('Jake', CURRENT_DATE, 'M', 'Rua 2', 2);
INSERT INTO public.empregados (nome, data_registro, sexo, endereco, supervisor_id) VALUES('Ana', CURRENT_DATE, 'F', 'Rua 3', 2);


-- Inserindo informacao de dependente
ALTER TABLE empregados 
ADD COLUMN dependente_id INT,
ADD CONSTRAINT fk_dependente
    FOREIGN KEY (dependente_id)
    REFERENCES dependentes(dependente_id);
   
-- Inserindo informacao de departamento
ALTER TABLE empregados 
ADD COLUMN departamento_id INT,
ADD CONSTRAINT fk_departamento
    FOREIGN KEY (departamento_id)
    REFERENCES departamentos(departamento_id);
   
-- Inserindo informacao de projetos
ALTER TABLE empregados 
ADD COLUMN projeto_id INT,
ADD CONSTRAINT fk_projeto
    FOREIGN KEY (projeto_id)
    REFERENCES projetos(projeto_id);
   
   
-- Atualizando informacao de parentesco
UPDATE public.empregados SET dependente_id = (SELECT dependente_id  FROM dependentes d WHERE  d.nome = 'Verena') WHERE empregado_id = 2;
UPDATE public.empregados SET dependente_id = (SELECT dependente_id  FROM dependentes d WHERE  d.nome = 'Floquinho') WHERE empregado_id = 3;

-- Atualizando departamentos
UPDATE  empregados SET departamento_id = (SELECT departamento_id  FROM departamentos  d WHERE  d.nome = 'Diretoria') where empregado_id = 2;
UPDATE  empregados SET departamento_id = (SELECT departamento_id  FROM departamentos  d WHERE  d.nome = 'QA') where empregado_id = 3;
UPDATE  empregados SET departamento_id = (SELECT departamento_id  FROM departamentos  d WHERE  d.nome = 'Desenvolvimento') where empregado_id = 4;

UPDATE empregados  SET projeto_id = (SELECT projeto_id  FROM projetos p WHERE  p.nome = 'Super Nintendo' )

 -- Consultando dados na tabela
SELECT * FROM public.empregados order by empregado_id 

-- Consulta de gerente e departamento
select e.empregado_id as id, e.nome as nome, d.nome as nome_departamento from empregados e join departamentos d on e.empregado_id  = d.gerente_id  