import reflex as rx
import os

db_url = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:Vv-32273930@db.uofdsyafzndqzhxvaprf.supabase.co:5432/postgres")

config = rx.Config(
    app_name="pagina_web",
    db_url=db_url,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
