
# Projeto de Autenticação com FastAPI, Redis e PostgreSQL

Este é um projeto simples de autenticação utilizando FastAPI, Redis e PostgreSQL. O objetivo deste projeto é servir como uma introdução ao desenvolvimento de aplicações web com autenticação baseada em sessões. O projeto inclui endpoints para registro, login e logout de usuários.

## Funcionalidades
- Validação de senha forte
- Registro de usuário com criptografia de senhas (usando bcrypt)
- Validação de email (regex e verificação de DNS)
- Login de usuário
- Proteção de rotas com sessões
- Logout de usuário (futuro)
- Suporte PostgreSQL usando SQLAlchemy

## Tecnologias Utilizadas

- **Backend**: FastAPI
- **Banco de Dados**: PostgreSQL usando SQLAlchemy
- **Gerenciamento de Sessão**: Redis
- **Criptografia de Senhas**: bcrypt
- **Frontend**: HTML, CSS e JavaScript
- **Validação de Email**: `email-validator`

## Estrutura do Projeto

```
├── app
│   ├── database
│   │   ├── redis.py
│   │   └── sql.py
│   ├── main.py
│   ├── responses
│   │   └── users.py
│   ├── routers
│   │   ├── __init__.py
│   │   └── users.py
│   ├── schemas
│   │   └── users.py
│   ├── static
│   │   ├── index.css
│   │   ├── login.js
│   │   └── signup.js
│   ├── templates
│   │   ├── login.html
│   │   ├── logout.html
│   │   └── register.html
│   └── views
│       └── view.py
├── docker-compose.yaml
├── LICENSE
├── pyproject.toml
├── README.md
├── requeriments.txt
└── tests
    ├── __init__.py
    └── test_app.py
```

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie um ambiente virtual e instale as dependências:

```bash
poetry install
poetry shell
```

3. Execute a aplicação FastAPI:

```bash
task run
```

4. Acesse a documentação interativa ou de leitura da API:

```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

```

## Endpoints

### Registro de Usuário

`POST /users/signup`

- Request Body: 
  ```json
  {
    "name": "string",
    "email": "string",
    "username": "string",
    "passwd": "string"
  }
  ```
- Lógica de Registro:
  - Verifica se o usuário já existe no banco de dados.
  - Valida o email usando regex e verificações de DNS com a biblioteca `email-validator`.
  - Criptografa a senha antes de armazená-la no banco de dados.
- Response:
  - `201 Created`: Registro bem-sucedido
  - `303 See Other`: Usuário já existe

### Login de Usuário

`POST /users/signin`

- Request Body:
  ```json
  {
    "username": "string",
    "passwd": "string"
  }
  ```
- Response:
  - `200 OK`: Login bem-sucedido
  - `401 Unauthorized`: Usuário não encontrado

### Verificação de Sessão

`GET /users/user`

- Response:
  - `200 OK`: Sessão válida
  - `401 Unauthorized`: Sessão inválida ou não encontrada

## Testes

Para rodar os testes, utilize o comando:

```bash
pytest
```

## Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para a sua feature (`git checkout -b feature/fooBar`)
3. Faça commit das suas alterações (`git commit -am 'Add some fooBar'`)
4. Faça push para a branch (`git push origin feature/fooBar`)
5. Crie um novo Pull Request

## Aprendizado

Este projeto é ideal para aprender e praticar:

- Estruturação de projetos web com FastAPI
- Utilização de Redis para gerenciamento de sessões
- Criação de uma interface web básica com HTML, CSS e JavaScript
- Práticas de autenticação e autorização
- Validação de email e criptografia de senhas
- Migração de banco de dados de SQLite para PostgreSQL com SQLAlchemy

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## Contato

Isack Vitor - [Telegram](https://t.me/lzaacFoster), [Linkedin](https://www.linkedin.com/in/isack-foster/) - isack200961@hotmail.com

Link do Projeto: [fastapi-login-boilerplate](https://github.com/Isaac-Foster/fastapi-login-boilerplate)
