import pytest
from sqlalchemy import text

from src.pipeline.database_connection import engine_postgresql


def test_database_connection():
    """Testa se a conexão ao banco pode ser estabelecida."""
    try:
        with engine_postgresql.connect() as conn:
            result = conn.execute(text('SELECT 1;'))  # 🔹 Usando text() corretamente
            assert result.scalar() == 1
    except Exception as e:
        pytest.fail(f'Falha ao conectar ao banco: {e}')
