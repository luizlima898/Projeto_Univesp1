CREATE DATABASE IF NOT EXISTS estoque;
USE estoque;
CREATE TABLE IF NOT EXISTS estoque( codigo INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR (200), estoque INT, local VARCHAR (100));
INSERT INTO estoque (codigo, nome, estoque, local) VALUES (1, 'PORTA DE FERRO ALZ', 50, 'BOX 10');
