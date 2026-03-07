import reflex as rx
import os

# 1. Obtenemos la URL de la variable de entorno
raw_db_url = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:Vv-32273930@db.uofdsyafzndqzhxvaprf.supabase.co:5432/postgres"
)

# 2. Corrección de compatibilidad para SQLAlchemy y Render
# Cambiamos postgres:// por postgresql+psycopg2:// si es necesario
if raw_db_url.startswith("postgresql://"):
    db_url = raw_db_url.replace("postgresql://", "postgresql+psycopg2://", 1)
elif raw_db_url.startswith("postgres://"):
    db_url = raw_db_url.replace("postgres://", "postgresql+psycopg2://", 1)
else:
    db_url = raw_db_url

config = rx.Config(
    app_name="pagina_web",
    db_url=db_url,
    plugins=[
        rx.plugins.SitemapPlugin(),
        # Nota: Asegúrate de que TailwindV4 sea compatible con tu versión de Reflex
        rx.plugins.TailwindV4Plugin(),
    ]
)
