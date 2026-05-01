import reflex as rx
from .styles import *

def boton_whatsapp() -> rx.Component:
    """Botón flotante de contacto directo vía WhatsApp."""
    return rx.link(
        rx.image(
            src="/whatsapp_logo.png",
            width=rx.breakpoints(initial="45px", sm="60px"),
            height="auto",
            _hover={"transform": "scale(1.1)"},
            transition="transform 0.2s",
        ),
        href=f"https://wa.me/{PHONE_NUMBER}",
        is_external=True,
        aria_label="Contáctame por WhatsApp",
    )

def menu_navegacion() -> rx.Component:
    """Barra de navegación superior estilizada."""
    enlaces = [
        ("INICIO", "/"),
        ("SOBRE MÍ", "/sobre-mi"),
        ("PROYECTOS", "/proyectos"),
        ("LENGUAJES", "/lenguajes"),
    ]
    return rx.box(
        rx.hstack(
            *[
                rx.link(
                    texto, 
                    href=ruta, 
                    text_decoration="none",
                    color="white",
                    font_weight="bold",
                    font_size=rx.breakpoints(initial="0.75em", sm="0.9em"),
                    _hover={"color": COLOR_ACCION}
                ) for texto, ruta in enlaces
            ],
            spacing=rx.breakpoints(initial="4", sm="9"),
            align_items="center",
            padding_y="1em",
            padding_x=rx.breakpoints(initial="1.5em", sm="2em"),
            background="rgba(15, 15, 15, 0.65)",
            backdrop_filter="blur(16px)",
            border="1px solid rgba(255, 255, 255, 0.08)",
            border_radius="full",
            box_shadow="0 8px 32px 0 rgba(0, 0, 0, 0.3)",
            pointer_events="auto",
            width=rx.breakpoints(initial="90%", sm="auto"),
        ),
        position="fixed",
        top="30px",
        left="0",
        right="0",
        z_index="1000",
        display="flex",
        justify_content="center",
        width="100%",
        pointer_events="none",
    )

# Lógica de animación Matrix en JS
JS_MATRIX = """
if (typeof window.initMatrix === 'undefined') {
    window.initMatrix = () => {
        const canvas = document.getElementById('matrix-canvas');
        if (!canvas || canvas.getAttribute('data-initialized') === 'true') return;
        canvas.setAttribute('data-initialized', 'true');

        const ctx = canvas.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;

        const fontSize = 14;
        const columns = Math.floor(width / fontSize);
        const drops = Array(columns).fill(1);

        const draw = () => {
            if (!document.body.contains(canvas)) return;
            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, width, height);
            ctx.fillStyle = "#00BFFF";
            ctx.font = fontSize + "px monospace";

            for (let i = 0; i < drops.length; i++) {
                const text = Math.random() > 0.5 ? "0" : "1";
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                if (drops[i] * fontSize > height && Math.random() > 0.975) drops[i] = 0;
                drops[i]++;
            }
            requestAnimationFrame(draw);
        };
        draw();

        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            canvas.width = width;
            canvas.height = height;
        });
    };
    setInterval(window.initMatrix, 100);
}
"""

def fondo_animado() -> rx.Component:
    """Componente que inyecta el canvas y el script de Matrix."""
    return rx.fragment(
        rx.script(JS_MATRIX),
        rx.html('<canvas id="matrix-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer_events: none;"></canvas>')
    )

def layout_base(contenido: rx.Component) -> rx.Component:
    """Estructura base que envuelve cada página, incluyendo el fondo Matrix y la navegación."""
    return rx.box(
        fondo_animado(),
        rx.box(
            menu_navegacion(),
            rx.box(
                contenido,
                width="100%",
                display="flex",
                justify_content="center",
            ),
            rx.box(
                boton_whatsapp(),
                position="fixed",
                bottom=rx.breakpoints(initial="20px", sm="30px"),
                right=rx.breakpoints(initial="20px", sm="30px"),
                z_index="1000",
            ),
            position="relative",
            z_index="1",
            background="rgba(0, 0, 0, 0.3)",
            width="100%",
            padding_x=rx.breakpoints(initial="1em", sm="2em", lg="4em"),
        ),
        width="100%",
        overflow_x="hidden",
        min_height="100vh",
        background_color="black",
    )