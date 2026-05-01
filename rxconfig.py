import reflex as rx
import os


config = rx.Config(
    app_name="pagina_web",
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
