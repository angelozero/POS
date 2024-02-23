DROP SCHEMA
CREATE SCHEMA
SET SCHEMA 'carros';
SET
CREATE TABLE carros.automoveis (
    codigo integer NOT NULL,
    ano character(2) NOT NULL,
    fabricante character(20),
    modelo character(20),
    preco_tabela numeric(8,2),
    pais character(20)
);
CREATE TABLE
CREATE TABLE carros.consumidores (
    cpf character(12) NOT NULL,
    nome character(15),
    sobrenome character(15),
    cidade character(25),
    estado character(2)
);
CREATE TABLE
CREATE TABLE carros.garagens (
    codigo integer NOT NULL,
    ano character(2) NOT NULL,
    cgc integer NOT NULL,
    quantidade integer
);
CREATE TABLE
CREATE TABLE carros.negocios (
    codigo integer NOT NULL,
    ano character(2) NOT NULL,
    cgc integer NOT NULL,
    cpf character(12) NOT NULL,
    data date,
    preco numeric(8,2)
);
CREATE TABLE
CREATE TABLE carros.revendedoras (
    cgc integer NOT NULL,
    nome character(20),
    estado character(2),
    cidade character(25),
    proprietario character(12)
);


INSERT INTO carros.automoveis VALUES (1022, '85', 'Ford', 'Del Rey', 4800.00, 'EUA');
INSERT INTO carros.consumidores VALUES ('5755-5', 'Mario', 'Amato', 'Sao Paulo', 'SP');
INSERT INTO carros.garagens VALUES (1051, '88', 10780, 2);
INSERT INTO carros.negocios VALUES (1111, '95', 10460, '7685-5      ', '1995-08-15', 8250.00);
INSERT INTO carros.revendedoras VALUES (10330, 'Dirija', 'RJ', 'Campos', '5698-8');