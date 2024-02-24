-- criando tabela de dependentes
CREATE TABLE public.dependentes (
	dependente_id serial PRIMARY KEY,
    nome character(20) NOT NULL,
    parentesco character(20),
    sexo character(2)
);


-- removendo a restrição de chave primária existente
ALTER TABLE dependentes DROP CONSTRAINT IF EXISTS dependentes_pkey;

-- Adicionando a nova coluna
ALTER TABLE dependentes
ADD COLUMN cpf INT;

-- definindo nova chave primária composta
ALTER TABLE dependentes
ADD PRIMARY KEY (dependente_id, cpf);


INSERT INTO public.dependentes (nome, parentesco, sexo) VALUES('Floquinho', 'Irmão', 'M');
INSERT INTO public.dependentes (nome, parentesco, sexo) VALUES('Verena', 'Irmã', 'F');

SELECT  * FROM dependentes