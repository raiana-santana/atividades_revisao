-- criando uma tabela no mysql
CREATE TABLE usuarios(
    nome VARCHAR(50),
    email VARCHAR(100),
    idade INT
);

-- inserindo linhas nas colunas da tabela. perceba que a inserção de dados deve seguir a ordem definida (no caso abaixo: nome, email, idade)
INSERT INTO usuarios(nome, email, idade) VALUES(
    "Raiana Santana",
    "raiana@email.com",
    24
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Andressa Brito",
    "andressa@email.com",
    24
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Roque Junior",
    "roque@email.com",
    28
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Mariana Oliveira",
    "mari@email.com",
    23
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Cleisa Santana",
    "cleisa@email.com",
    24
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Mahara Rezende",
    "mahara@email.com",
    23
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Fabiana Lisboa",
    "fafa@email.com",
    29
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Gabriel Santana",
    "biel@email.com",
    17
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Maria Alice",
    "lilica@email.com",
    2
);

-- mostrando apenas as informações/usuarios que tem a idade = 24
SELECT * FROM usuarios WHERE idade = 24;

-- mostrando apenas as informações/usuarios que tem a nome = "Raiana Santana"
SELECT * FROM usuarios WHERE nome = "Raiana Santana";

-- mostrando apenas as informações/usuarios que tem a idade >= 24
SELECT * FROM usuarios WHERE idade >= 18;

-- deletando um usuário em específico (no caso abaixo, o usuário que tem nome = "Maria Alice")
DELETE FROM usuarios WHERE nome = "Maria Alice";

-- atualizando algum dado na tabela
UPDATE usuarios SET nome = "Nome de Teste" WHERE nome = "Fabiana Lisboa";