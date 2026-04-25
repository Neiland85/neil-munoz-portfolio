import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

# 1. Añadimos 'src' al path para poder importar módulos de FastAPI
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

# 2. IMPORTANTE: Importa aquí tu Base o SQLModel
from sqlmodel import SQLModel

# Importamos el paquete de modelos completo para registrar todos los modelos a la vez
import app.models  # noqa
from app.core.config import get_settings

target_metadata = SQLModel.metadata

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

settings = get_settings()


def run_migrations_offline() -> None:
    """Ejecuta las migraciones en modo 'offline' (generación de scripts)."""
    url = str(settings.DATABASE_URL)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecuta las migraciones en modo 'online' (aplicar a base de datos)."""
    configuration = config.get_section(config.config_ini_section) or {}
    configuration["sqlalchemy.url"] = str(settings.DATABASE_URL)

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
