# Criação  backend completo - Delivery de pizzaria + JWT
- Integração com banco de dados;
- Criação de endpoint com FastAPI (endpoint ordens e auth);
- Todo processo de criação de usuário e login;
- Autenticação com JWT.


## Install Dependencies
`pip install -r requirements.txt`

## Activate virtual enviroments
`source .venv/bin/activate.fish`

## Run the project:
`uvicorn main:app --reload`

## alembic config initial
`alembic init alembic`

## run migration
`alembic revision --autogenerate -m <message>`

## exec migration
`alembic upgrade head`

