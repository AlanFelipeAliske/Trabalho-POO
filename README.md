# Trabalho-POO

### CheckList de equipamentos de segurança

Proposta: 
Criar um programa em linguagem orientada a objetos que implemente as classes mostradas no diagrama abaixo, preferencialmente com uso de dados em banco de dados, e permita ao usuário
fornecer e consultar os dados das classes.
A equipe poderá escolher a linguagem (orientada a objetos) que desejar, e uma das plataformas
{console, janelas, web ou mobile}.

Programa foi desenvolvido utilizando o framework Django com linguagem Python


## Documentação

[Link da Documentação do Django](https://docs.djangoproject.com/pt-br/4.0/intro/tutorial01/)


## Passo a passo para configurar o ambiente e rodar o projeto (Windows)

Ter o Python instalado e atualizado

Prompt de comando como administrador

Criando a venv caso não tenha.

Comando:
python -m venv venv 

ir até a pasta:
( \venv\Scripts )
rodar o comando activate.bat

Com a venv rodando ir até a pasta:
( Trabalho-POO\AppDjango )

E rodar os seguinter comandos:
python -m pip install --upgrade pip
pip install -r requirements.txt

Se precisar atualizar, usar o comando abaixo
pip upgrade -r requirements.txt

Para rodar a aplicação:
python manage.py runserver

Criando um super usuário:
python manage.py createsuperuser


## Funcionalidades

- Adicionar Veículos
- Adicionar equipamentos
- Criar checklists de veículos
- Administrar o sistema

