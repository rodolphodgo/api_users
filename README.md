# API de Gerenciamento de Usuários

Este projeto é uma API REST desenvolvida com FastAPI e SQLAlchemy para gerenciar usuários. A aplicação oferece rotas para criar, ler, atualizar e deletar, utilizando banco de dados SQLite para persistência dos dados.

## Funcionalidades

* **Listar todos os usuários:** Retorna todos os usuários cadastrados.
* **Buscar usuários por ID:** Retorna um usuário específico com base no ID.
* **Criar novo usuário:** Permite adicionar novos usuários ao banco.
* **Atualizar usuários por ID:** Atualiza um usuário específico com base no ID.
* **Deletar usuário por ID:** Permite remover um usuário do banco.

## Tecnologias

* Python
* FastAPI
* SQlAlchemy
* Pydantic
* SQLLite
* UUID
* Pendulum

## Pré-Requisitos

Para rodar o projeto, é preciso ter o Python 3.7+ instalado.

## Dependências

As dependências do projeto estão listadas no arquivo requirements.txt.

## Para Iniciar o Projeto

**1. Clonar o repositório**

* Primeiro, clone o projeto para o seu ambiente local.

**2. Criar e Ativar o Ambiente Virtual**

* Criar: python -m venv venv
* Ativar (Windowns): venv\Scripts\activate
* Ativar (macOS/Linux): source venv/bin/activate

**3. Installar as Dependências**

* pip install -r requirements.txt

**4. Executar a Aplicação**

* uvicorn main:app --reload

**5. Acessar a Documentação Swager**

* Adcionar "/docs" na porta: http://127.0.0.1:8000/docs