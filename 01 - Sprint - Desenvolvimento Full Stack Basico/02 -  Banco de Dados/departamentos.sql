CREATE TABLE public.departamentos (
	departamento_id serial PRIMARY KEY,
    nome character(20) NOT NULL

);


-- Adicionando relacao de gerencia
ALTER TABLE public.departamentos 
ADD CONSTRAINT departamentos_fk 
FOREIGN KEY (gerente_id) REFERENCES public.empregados(empregado_id);



INSERT INTO public.departamentos (nome) VALUES('Desenvolvimento');
INSERT INTO public.departamentos (nome) VALUES('Diretoria');
INSERT INTO public.departamentos (nome) VALUES('QA');

UPDATE  departamentos SET gerente_id = (SELECT empregado_id  FROM empregados d WHERE  d.nome = 'Ana') where nome = 'QA';

SELECT * FROM departamentos p 