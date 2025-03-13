import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from urllib.parse import quote

# Carregar as variáveis do .env
load_dotenv()

# Configurações do banco PostgreSQL
POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")
POSTGRESQL_PORT = os.getenv("POSTGRESQL_PORT")
POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")
POSTGRESQL_DATABASE = os.getenv("POSTGRESQL_DATABASE")
POSTGRESQL_PASSWORD = quote(os.getenv("POSTGRESQL_PASSWORD"))

POSTGRE_URL = (
    f"postgresql+psycopg2://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}"
    f"@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DATABASE}"
)

# Criar o motor de conexão para o Postgresql
engine_postgresql = create_engine(POSTGRE_URL)

# Criar a fábrica de sessões para o Postgresql
SessionPostgresql = sessionmaker(bind=engine_postgresql)