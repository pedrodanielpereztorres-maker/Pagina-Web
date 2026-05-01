import reflex as rx
from .styles import *
from .componentes import layout_base

# --- VISTAS / PÁGINAS ---
# Definición del estado para manejar la galería de imágenes de los proyectos

class ProyectosState(rx.State):
    modal_abierto: bool = False
    titulo_seleccionado: str = ""
    imagenes_seleccionadas: list[str] = []

    def ver_galeria(self, proyecto: dict[str, any]) -> None:
        """Abre el modal y carga las imágenes del proyecto seleccionado."""
        self.titulo_seleccionado = str(proyecto.get("titulo", ""))
        self.imagenes_seleccionadas = list(proyecto.get("imagenes", []))
        self.modal_abierto = True

    def cerrar_galeria(self) -> None:
        """Cierra el modal de la galería."""
        self.modal_abierto = False

def pagina_inicio() -> rx.Component:
    """Contenido de la página principal."""
    return layout_base(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Soy Pedro Pérez", 
                    color=COLOR_ACCION, 
                    font_size=TAMANIO_TITULO_HERO,
                    font_family=FUENTE_TITULOS,
                    letter_spacing=LETTER_SPACING_HERO,
                    line_height="1.2", # Asegura que el texto no colapse sobre sí mismo
                    text_shadow=f"0 0 20px {COLOR_ACCION}4D", # Sombra sutil de color
                    transition="all 0.3s ease",
                   
                    _hover={
                        "text_shadow": f"0 0 30px {COLOR_ACCION}, 0 0 60px {COLOR_ACCION}",
                        "transform": "scale(1.02)",
                    },
                ),
                rx.heading(
                    "Analista de sistemas y Programador", 
                    color="rgba(255, 255, 255, 0.9)", 
                    font_size=TAMANIO_SUBTITULO, 
                    font_family=FUENTE_TITULOS,
                    letter_spacing=LETTER_SPACING_SUB,
                    font_weight="500", 
                    line_height="1.2",
                    text_align="center",
                    text_shadow=f"0 0 15px {COLOR_ACCION}33", # Brillo sutil para armonizar
                ),
                rx.text(
                    "Apasionado por crear aplicaciones web elegantes y automatizar procesos.",
                    color=TEXTO_SECUNDARIO,
                    font_size=TEXTO_RESPONSIVO,
                    font_family=FUENTE_CUERPO,
                    text_align="center",
                    max_width="800px",
                    line_height="1.4",
                    font_weight="300",
                    letter_spacing="0.8px",
                    opacity="0.85",
                ),
                spacing="2", # Reducimos el espacio entre elementos para compactar el diseño en PC
                min_height="100vh",
                justify="center",
                padding_top=rx.breakpoints(initial="20px", sm="0px"), # Ajustado para que no se vea tan abajo en móviles
               
            )
        )
    )

def pagina_sobre_mi() -> rx.Component:
    """Vista biográfica del perfil."""
    return layout_base(
        rx.vstack(
            rx.heading(
                "Sobre Mí", # Título principal de la sección
                color="white", 
                font_size=TAMANIO_TITULO_SECCION, 
                font_family=FUENTE_TITULOS,
                text_align="center",
                letter_spacing="2px",
                line_height="1.4",
                text_shadow=f"0 0 20px {COLOR_ACCION}33",
            ),
            rx.vstack(
                rx.text(
                    "Soy Pedro Pérez, estudiante de Análisis de Sistemas en el IUTEPI (5to semestre) con experiencia práctica en el desarrollo de sistemas de gestión completos para entornos institucionales reales. Me apasiona la programación, el desarrollo de software y todo lo que tenga que ver con tecnología e innovación. Disfruto aprender constantemente: cada nuevo framework, patrón de diseño o herramienta es una oportunidad para construir mejores soluciones. Mi enfoque está en la arquitectura de software: diseño esquemas de base de datos relacionales normalizados, estructuro aplicaciones bajo patrones MVC y desarrollo interfaces funcionales con Python, Reflex y PostgreSQL. No trabajo solo con código de práctica — he construido y desplegado sistemas en producción que están actualmente en uso en instituciones reales. Busco seguir creciendo en desarrollo full-stack y arquitectura de sistemas, aportando soluciones técnicas sólidas, mantenibles y orientadas al impacto real.",
                    color=TEXTO_SECUNDARIO,
                    text_align="justify",
                    line_height="1.6",
                    margin_bottom="1.5em",
                ),
                # Grid de información complementaria para llenar el espacio de forma profesional
                rx.grid(
                    rx.vstack(
                        rx.hstack(rx.icon("briefcase", color=COLOR_ACCION, size=20), rx.heading("Experiencia", size="4", color="white")),
                        rx.text("Desarrollo e implementación de sistemas de gestión institucional, incluyendo módulos de inventario, control de usuarios y autenticación segura.", size="2", color=TEXTO_SECUNDARIO),
                        align_items="start",
                        spacing="2",
                    ),
                    rx.vstack(
                        rx.hstack(rx.icon("graduation-cap", color=COLOR_ACCION, size=20), rx.heading("Educación", size="4", color="white")),
                        rx.text("Técnico Superior en Análisis de Sistemas — IUTEPI (en curso, 5to semestre).", size="2", color=TEXTO_SECUNDARIO),
                        align_items="start",
                        spacing="2",
                    ),
                    rx.vstack(
                        rx.hstack(rx.icon("code_xml", color=COLOR_ACCION, size=20), rx.heading("Especialidad", size="4", color="white")),
                        rx.text("Arquitectura de software, patrones MVC y diseño de bases de datos relacionales normalizadas.", size="2", color=TEXTO_SECUNDARIO),
                        align_items="start",
                        spacing="2",
                    ),
                    columns=rx.breakpoints(initial="1", sm="3"),
                    spacing="6",
                    width="100%",
                    margin_bottom="2em",
                ),
                rx.divider(border_color="rgba(255,255,255,0.1)", width="100%"),
                # Enlaces de contacto/redes dentro de la tarjeta
                rx.hstack(
                    rx.link(
                        rx.icon("github", size=20),
                        href=f"https://github.com/{GITHUB_USER}",
                        color=TEXTO_SECUNDARIO,
                        _hover={"color": COLOR_ACCION},
                        is_external=True,
                    ),
                    rx.link(
                        rx.icon("message-circle", size=20),
                        href=f"https://wa.me/{PHONE_NUMBER}",
                        color=TEXTO_SECUNDARIO,
                        _hover={"color": COLOR_ACCION},
                        is_external=True,
                    ),
                    rx.link(
                        rx.icon("mail", size=20),
                        href=f"mailto:{EMAIL_ADDRESS}",
                        color=TEXTO_SECUNDARIO,
                        _hover={"color": COLOR_ACCION},
                        is_external=True,
                    ),
                    spacing="6",
                    margin_top="1.5em",
                ),

                align_items="center",
                padding=rx.breakpoints(initial="20px", sm="40px"),
                background=FONDO_TARJETA,
                border=BORDE_FINO,
                border_radius="20px",
                backdrop_filter="blur(10px)",
            ),

            width="100%",
            max_width="900px",
            padding_top=ESPACIADO_TOP_PAGINA,
            padding_bottom="100px",
            align_items="center",
            spacing="8",
        )
    )

def pagina_proyectos() -> rx.Component:
    """Galería de trabajos realizados."""
    def tarjeta(p: dict[str, any]) -> rx.Component:
        """Renderiza una tarjeta individual de proyecto con efecto Glassmorphism."""
        return rx.box(
            rx.vstack(
                rx.box(
                    # Cabecera simulada de ventana de aplicación para dar contexto al sistema
                    rx.hstack(
                        rx.box(width="8px", height="8px", border_radius="full", bg="#ff5f57"),
                        rx.box(width="8px", height="8px", border_radius="full", bg="#ffbd2e"),
                        rx.box(width="8px", height="8px", border_radius="full", bg="#28c940"),
                        spacing="2",
                        padding="10px 14px",
                        background="rgba(255, 255, 255, 0.05)",
                        width="100%", 
                    ),
                    rx.box(
                        rx.image(
                            src=p["img"], 
                            width="100%", 
                            height="240px", 
                            object_fit="cover",
                            object_position="center", 
                            transition="all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1)",
                            style={
                                "filter": "brightness(0.95) contrast(1.05)",
                                "backface-visibility": "hidden",
                                "transform": "translateZ(0)",
                                "-webkit-font-smoothing": "subpixel-antialiased",
                            },
                            _hover={"transform": "scale(1.05)", "filter": "brightness(1.05) contrast(1.1)"},
                            loading="lazy",
                        ),
                        overflow="hidden",
                    ),
                    width="100%",
                    border_radius="12px 12px 0 0",
                    border_bottom=f"1px solid rgba(255, 255, 255, 0.1)",
                ),
                rx.vstack(
                    rx.heading(p["titulo"], size="5", color="white", font_family=FUENTE_TITULOS, font_weight="700"),
                    rx.text(p["desc"], color=TEXTO_SECUNDARIO, size="2", line_height="1.6", opacity="0.8"),
                    rx.flex(
                        *[
                            rx.badge(p[k], variant="soft", color_scheme=color, border_radius="lg", size="1", padding_x="0.6em")
                            for k, color in [("lenguaje", "blue"), ("framework", "cyan"), ("bd", "purple")]
                            if p.get(k)
                        ],
                        flex_wrap="wrap",
                        spacing="2",
                        margin_top="0.8em",
                    ),
                    rx.spacer(),
                    rx.hstack(
                        rx.text("Ver galería", size="1", color=COLOR_ACCION, font_weight="bold"),
                        rx.icon("arrow-right", size=14, color=COLOR_ACCION),
                        spacing="2",
                        align_items="center",
                        width="100%",
                        justify="end",
                    ),
                    padding="1.5em",
                    align_items="start",
                    spacing="3",
                    height="100%",
                ),
                spacing="0",
                height="100%",
            ),
            background="rgba(255, 255, 255, 0.02)",
            border=BORDE_FINO,
            border_radius="15px",
            on_click=lambda: ProyectosState.ver_galeria(p),
            cursor="pointer",
            transition="all 0.3s ease",
            _hover={
                "transform": "translateY(-8px)", 
                "border": f"1px solid {COLOR_ACCION}44",
                "box_shadow": f"0 20px 40px -12px {COLOR_ACCION}22",
                "background": "rgba(255, 255, 255, 0.06)",
            },
            backdrop_filter="blur(12px)",
            height="100%",
        )

    return layout_base(
        rx.vstack(
            rx.heading(
                "Portafolio de Proyectos", 
                color="white", 
                font_size=TAMANIO_TITULO_SECCION, 
                font_family=FUENTE_TITULOS
            ),
            rx.vstack(
                rx.text(
                    "Una selección de mis trabajos más destacados en desarrollo y análisis.", 
                    color=TEXTO_SECUNDARIO, 
                    font_size="1.1em",
                    opacity="0.8"
                ),
                rx.box(width="50px", height="2px", bg=COLOR_ACCION, margin_top="1em"),
                align_items="center",
                margin_bottom="3em",
            ),
            rx.grid(
                *[tarjeta(p) for p in DATOS_PROYECTOS],
                columns=rx.breakpoints(initial="1", sm="2", lg="3"),
                spacing="6",
                width="100%",
            ),
            rx.dialog.root(
                rx.dialog.content(
                    rx.hstack(
                        rx.dialog.title(
                            ProyectosState.titulo_seleccionado,
                            color=COLOR_ACCION,
                            font_family=FUENTE_TITULOS,
                            size="6",
                        ),
                        rx.spacer(),
                        rx.dialog.close(
                            rx.button(
                                rx.icon("x"), 
                                variant="ghost", 
                                color_scheme="gray",
                                on_click=ProyectosState.cerrar_galeria
                            )
                        ),
                        width="100%",
                        align_items="center",
                        margin_bottom="1em",
                    ),
                    rx.dialog.description(
                        "Visualización detallada del proyecto. Desliza para ver todas las capturas.",
                        color=TEXTO_SECUNDARIO,
                        margin_bottom="1.5em",
                        font_size="0.9em",
                    ),
                    rx.scroll_area(
                        rx.vstack(
                            rx.foreach(
                                ProyectosState.imagenes_seleccionadas,
                                lambda img: rx.box(
                                    rx.image(
                                        src=img, 
                                        width="100%", 
                                        border_radius="12px",
                                        border="1px solid rgba(255,255,255,0.1)",
                                        margin_bottom="1.5em",
                                        box_shadow="lg",
                                    ),
                                    width="100%",
                                )
                            ),
                            width="100%",
                            padding_right="1em",
                        ),
                        style={"max_height": "60vh"},
                        scrollbars="vertical",
                    ),
                    size="4",
                    background="rgba(10, 10, 10, 0.98)",
                    backdrop_filter="blur(20px)",
                    border=f"1px solid {COLOR_ACCION}44",
                    padding="2em",
                    max_width="900px",
                    border_radius="24px",
                ),
                open=ProyectosState.modal_abierto,
                on_open_change=lambda _: ProyectosState.cerrar_galeria(),
            ),
            width="100%",
            max_width="1200px",
            align_items="center",
            padding_top=ESPACIADO_TOP_PAGINA,
            padding_bottom="100px",
        )
    )

def pagina_lenguajes() -> rx.Component:
    """Sección de habilidades técnicas con logos animados."""
    def logo(item: dict[str, str]) -> rx.Component:
        """Renderiza un logo individual con su etiqueta correspondiente."""
        return rx.vstack(
            rx.center(
                rx.image(
                    src=item["src"],
                    alt=item["alt"],
                    width="auto",
                    height="auto",
                    max_width=rx.breakpoints(initial="50px", sm="70px"), 
                    max_height=rx.breakpoints(initial="50px", sm="70px"),
                    object_fit="contain",
                ),
                width=rx.breakpoints(initial="90px", sm="120px"),
                height=rx.breakpoints(initial="90px", sm="120px"),
                background="white",
                border_radius=rx.breakpoints(initial="15px", sm="20px"),
            ),
            rx.text(
                item["alt"],
                color="white",
                font_family=FUENTE_CUERPO,
                font_weight="bold",
                margin_top="0.8em",
                letter_spacing="1px",
                text_align="center",
            ),
            padding="1.5em",
            background=FONDO_TARJETA,
            border=BORDE_FINO,
            border_radius="xl",
            backdrop_filter="blur(10px)",
            transition="all 0.3s ease",
            width="100%", # Ajusta al ancho de la columna del grid
            height=rx.breakpoints(initial="180px", sm="240px"),
            _hover={
                "transform": "translateY(-10px)",
                "border_color": COLOR_ACCION,
                "box_shadow": f"0 15px 30px -10px {COLOR_ACCION}88",
                "background": "rgba(255, 255, 255, 0.06)",
            },
            align_items="center",
            justify_content="center",
        )

    return layout_base(
        rx.vstack(
            rx.heading(
                "Lenguajes y tecnologías que manejo", 
                color="white", 
                font_size=TAMANIO_TITULO_SECCION,
                font_family=FUENTE_TITULOS, 
                text_align="center",
                margin_bottom="2.5em",
            ),
            rx.grid(
                *[logo(l) for l in DATOS_LENGUAJES],
                columns=rx.breakpoints(initial="2", sm="3", md="3", lg="5"),
                spacing="5",
                width="100%",
            ),
            width="100%",
            max_width="1200px",
            padding_top=ESPACIADO_TOP_PAGINA,
            padding_bottom="100px",
            align_items="center",
            margin_x="auto",
        )
    )

# --- INICIALIZACIÓN DE LA APP ---

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Raleway:wght@300;400;700&display=swap",
        "/custom.css",
    ],
    style={
        "background_color": "black",
        "color": "white",
        "overflow_x": "hidden",
        "font_family": FUENTE_CUERPO,
        "-webkit-font-smoothing": "antialiased", # Mejora el renderizado de texto en Windows
        "-moz-osx-font-smoothing": "grayscale",
        "heading": {
            "font_family": FUENTE_TITULOS,
        },
        "::-webkit-scrollbar": {
            "width": "8px",
        },
        "::-webkit-scrollbar-track": {
            "background": "transparent",
        },
        "::-webkit-scrollbar-thumb": {
            "background": "rgba(255, 255, 255, 0.1)",
            "border_radius": "10px",
        },
        "::-webkit-scrollbar-thumb:hover": {
            "background": COLOR_ACCION,
        },
    }
)

# Registro de rutas vinculadas a sus respectivas funciones
app.add_page(
    pagina_inicio, 
    route="/", 
    title="Pedro Pérez | Analista de Sistemas",
    description="Portafolio profesional de Pedro Pérez, Analista de Sistemas y Programador."
)
app.add_page(
    pagina_sobre_mi, 
    route="/sobre-mi", 
    title="Sobre Mí | Pedro Pérez",
    description="Conoce más sobre la experiencia y educación de Pedro Pérez."
)
app.add_page(
    pagina_proyectos, 
    route="/proyectos", 
    title="Proyectos | Pedro Pérez",
    description="Galería de proyectos de desarrollo de software y sistemas de gestión."
)
app.add_page(
    pagina_lenguajes, 
    route="/lenguajes", 
    title="Tecnologías | Pedro Pérez",
    description="Lenguajes de programación y herramientas tecnológicas que manejo."
)
