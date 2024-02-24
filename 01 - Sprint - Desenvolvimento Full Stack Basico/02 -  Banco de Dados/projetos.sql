CREATE TABLE public.projetos (
	projeto_id serial PRIMARY KEY,
    nome character(20) NOT NULL
);

INSERT INTO public.projetos (nome) VALUES('Super Nintendo');

SELECT * FROM projetos p 