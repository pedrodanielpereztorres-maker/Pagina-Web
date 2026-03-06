import reflex as rx
import sqlmodel


@rx.ModelRegistry.register
class Usuarios(rx.Model, table=True):
    id_usuario: int | None = sqlmodel.Field(default=None, primary_key=True)
    nombre: str
    correo: str
    mensaje: str


class State(rx.State):
    dialog_open: bool = False
    show_success: bool = False
    form_data: dict = {}

    def set_dialog_open(self, open: bool):
        self.dialog_open = open
        if not open:
            self.show_success = False

    def submit_form(self, form_data: dict):
        self.form_data = form_data
        with rx.session() as session:
            session.add(
                Usuarios(
                    nombre=form_data["nombre"],
                    correo=form_data["correo"],
                    mensaje=form_data["mensaje"],
                )
            )
            session.commit()
        self.show_success = True


def contacto_form() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Contactar",
                background="linear-gradient(90deg, #00BFFF 0%, #0080FF 100%)",
                color="white",
                padding_x="30px",
                padding_y="25px",
                border_radius="30px",
                font_family="Arial, sans-serif",
                font_size="19px",
                font_weight="bold",
                _hover={
                    "transform": "scale(1.05)",
                    "boxShadow": "0 0 12px #00BFFF",
                },
            )
        ),
        rx.dialog.content(
            rx.cond(
                State.show_success,
                rx.vstack(
                    rx.dialog.title("¡Enviado con éxito!", color="#00BFFF", font_size=rx.breakpoints(
                        initial="24px", sm="25px", md="26px", lg="27px", xl="28px")),
                    rx.dialog.description(
                        "Gracias por contactarme.Te responderé pronto.",
                        color="white", font_size=rx.breakpoints(
                            initial="18px", sm="19px", md="20px", lg="21px", xl="22px"),
                        text_align="center",
                    ),
                    rx.dialog.close(
                        rx.button(
                            "Cerrar", background_color="#00BFFF", color="white"),
                        font_family="Arial, sans-serif",
                        font_size="16px",
                        font_weight="bold",
                        _hover={
                            "bg": "white",
                            "color": "#00BFFF",
                            "transform": "scale(1.05)",
                            "boxShadow": "0 0 12px #00BFFF",
                        },
                    ),
                    spacing="4",
                    align="center",
                ),
                rx.vstack(
                    rx.dialog.title("Contáctame", color="#00BFFF", font_size=rx.breakpoints(
                        initial="25px", sm="26px", md="27px", lg="28px", xl="29px")),
                    rx.dialog.description(
                        "Por favor completa el formulario para contactarme.",
                        color="white", font_size=rx.breakpoints(
                            initial="17px", sm="18px", md="19px", lg="20px", xl="22px")
                    ),
                    rx.form(
                        rx.vstack(
                            rx.input(
                                placeholder="Nombre",
                                name="nombre",
                                id="nombre",
                                required=True,
                                width="100%",
                                color="white",
                                bg="black",
                                border="2px solid #00BFFF",
                                border_radius="6px",
                                _focus={
                                    "border_color": "white",
                                    "box_shadow": "0 0 10px #00BFFF",
                                },
                                font_family="Arial, sans-serif",
                                class_name="form-input",
                            ),
                            rx.input(
                                placeholder="Correo Electrónico",
                                name="correo",
                                id="correo",
                                type_="email",
                                required=True,
                                width="100%",
                                color="white",
                                bg="black",
                                border="2px solid #00BFFF",
                                border_radius="6px",
                                _focus={
                                    "border_color": "white",
                                    "box_shadow": "0 0 10px #00BFFF",
                                },
                                font_family="Arial, sans-serif",
                                class_name="form-input",
                            ),
                            rx.text_area(
                                placeholder="Mensaje",
                                name="mensaje",
                                id="mensaje",
                                required=True,
                                width="100%",
                                height="150px",
                                color="white",
                                bg="black",
                                border="2px solid #00BFFF",
                                border_radius="6px",
                                _focus={
                                    "border_color": "white",
                                    "box_shadow": "0 0 10px #00BFFF",
                                },
                                font_family="Arial, sans-serif",
                                class_name="form-input",
                            ),
                            rx.button(
                                "Enviar",
                                type_="submit",
                                background="linear-gradient(90deg, #00BFFF 0%, #0080FF 100%)",
                                color="white",
                                width="100%",
                                font_family="Arial, sans-serif",
                                font_size="16px",
                                font_weight="bold",
                                _hover={
                                    "transform": "scale(1.05)",
                                    "boxShadow": "0 0 12px #00BFFF",
                                },
                            ),
                            spacing="4",
                        ),
                        on_submit=State.submit_form,
                        reset_on_submit=True,
                        width="100%",
                    ),
                    spacing="3",
                    color="white",
                ),
            ),
            bg="rgba(0, 0, 0, 0.8)",
            backdrop_filter="blur(10px)",
            border="1px solid rgba(255, 255, 255, 0.1)",

            padding=rx.breakpoints(initial="4", sm="5",
                                   md="6", lg="7", xl="8"),
            border_radius="10px",
            width="100%",
            max_width="600px",
        ),
        open=State.dialog_open,
        on_open_change=State.set_dialog_open,
    )


def texto_descripcion(texto: str) -> rx.Component:
    return rx.text(
        texto,
        color="#E0E0E0",
        font_size=rx.breakpoints(
            initial="1.1em", sm="1.2em", md="1.3em", lg="1.4em", xl="1.5em"),
        text_align="left",
        line_height="1.8",
        font_family="Raleway, sans-serif",
    )


def descripcion() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Sobre Mí", color="white",
                       size="8", margin_bottom="10px"),
            rx.vstack(
                texto_descripcion(
                    "Soy Pedro Pérez, analista de sistemas y apasionado por la innovación tecnológica."),
                texto_descripcion(
                    "Mi experiencia abarca desde el desarrollo modular en C++ y Python hasta la gestión de bases de datos SQL y NoSQL, siempre con el objetivo de crear soluciones sólidas, prácticas y con visión de futuro."),
                texto_descripcion(
                    "No me conformo con lo establecido: me gusta ir siempre más allá, romper los límites, porque estoy convencido de que uno no tiene límites."),
                texto_descripcion(
                    "Estoy aquí para transformar ideas en soluciones tecnológicas que marquen la diferencia."),
                texto_descripcion("Me considero un visionario tecnológico, alguien que combina lógica, creatividad y propósito para convertir ideas en realidades. Cada proyecto es para mí una oportunidad de innovar, de enseñar con claridad y de dejar huella en el camino."),
                spacing="4",
                padding=rx.breakpoints(initial="20px", sm="30px"),
                background="rgba(255, 255, 255, 0.03)",
                border="1px solid rgba(255, 255, 255, 0.1)",
                border_radius="20px",
                backdrop_filter="blur(10px)",
            ),
            id="sobre-mi",
            scroll_margin_top="6rem",
            max_width="800px",
            padding_y="70px",
        ),
        bg="transparent",
    )


def lenguajes_programacion() -> rx.Component:
    def logo(src: str, alt: str):
        return rx.image(
            src=src,

            width=["100px", "150px", "180px", "200px", "220px"],
            height=["100px", "150px", "180px", "200px", "220px"],
            border_radius="10px",
            alt=alt,
            animation="fade",
            style={
                "position": "relative",
                "transition": "transform 0.3s ease, box-shadow 0.3s ease",
                ":hover": {
                    "transform": "scale(1.02)",
                    "boxShadow": "0 0 10px 2px #00BFFF",
                    "z_index": "10",
                },
            },
        )
    return rx.box(
        rx.vstack(
            rx.heading(
                "Lenguajes Que Manejo:",
                style={
                    "fontFamily": "Raleway, sans-serif",

                },
                color="white",
                size="8",
                text_align="left",
                id="lenguajes",
            ),
            rx.box(
                rx.hstack(
                    logo(
                        "https://images.seeklogo.com/logo-png/47/1/microsoft-visual-basic-for-applications-logo-png_seeklogo-473389.png",
                        "Logo de VBA",
                    ),
                    logo(
                        "https://logowik.com/content/uploads/images/911_c_logo.jpg",
                        "Logo de C++",
                    ),
                    logo(
                        "https://logowik.com/content/uploads/images/python.jpg",
                        "Logo de Python",
                    ),
                    logo(
                        "https://tse2.mm.bing.net/th/id/OIP.8Lj00WWK8zjlatZq_m3nLgHaE8?rs=1&pid=ImgDetMain&o=7&rm=3",
                        "Logo adicional",
                    ),
                    logo(
                        "https://images.ctfassets.net/po4qc9xpmpuh/3DXFDcf1EO2D7mwb2r7RTM/62e5c1b9a070d21a0288d9dc9148a914/nosql.png",
                        "Logo NoSQL",
                    ),
                    spacing=rx.breakpoints(
                        initial="4", sm="4", md="6", lg="6", xl="6"),
                    flex_wrap="wrap",
                    justify="center",
                ),
                width="100%",
                z_index="5",
                position="relative",
            ),
            padding_y="50px",
            spacing="6",
            align_items="start",
        ),
    )


def menu() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.el.a("INICIO", href="#inicio", class_name="menu-link"),
            rx.el.a("SOBRE MÍ", href="#sobre-mi", class_name="menu-link"),
            rx.el.a("LENGUAJES", href="#lenguajes", class_name="menu-link"),
            spacing=rx.breakpoints(initial="4", sm="9"),
            justify="center",
            align_items="center",
            padding_x=rx.breakpoints(initial="1.5em", sm="3em"),
            padding_y="1em",
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


def index() -> rx.Component:
    return rx.fragment(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Soy Pedro Pérez",
                    color="#00BFFF",
                    style={
                        "fontFamily": "Cinzel, serif",
                        "letterSpacing": "4px",
                        "textShadow": "0 0 20px rgba(0, 191, 255, 0.3)",
                        "transition": "all 0.3s ease",
                    },
                    _hover={
                        "textShadow": "0 0 40px #00BFFF, 0 0 80px #00BFFF",
                        "transform": "scale(1.02)",
                    },
                    font_size=rx.breakpoints(
                        initial="40px", sm="50px", md="70px", lg="100px", xl="100px"),
                    text_align=rx.breakpoints(
                        initial="center", sm="center", md="center"),
                    margin_bottom=rx.breakpoints(lg="20px", xl="30px"),
                ),
                rx.heading(
                    "Analista de sistemas y Programador",
                    style={
                        "fontFamily": "Raleway, sans-serif",
                        "letterSpacing": "3px",
                        "fontWeight": "300",
                    },
                    size=rx.breakpoints(initial="6", sm="7",
                                        md="8", lg="9", xl="9"),
                    color="white",
                    text_align="center",
                ),
                rx.text(
                    "Apasionado por crear aplicaciones web elegantes, automatizar procesos y resolver problemas técnicos con precisión.",
                    color="#E0E0E0",
                    font_size=rx.breakpoints(
                        initial="1.1em", sm="1.2em", md="1.2em", lg="1.3em", xl="1.4em"),
                    text_align="center",
                    max_width="700px",
                    line_height="1.6",
                ),
                contacto_form(),
                spacing="5",
                justify="center",
                align="center",
                min_height="85vh",
                id="inicio",
                padding_top="80px",
            ),
            bg="transparent",
        ),
        descripcion(),
        lenguajes_programacion(),
        menu(),
    )


matrix_js = """
const initMatrix = () => {
    const canvas = document.getElementById('matrix-canvas');

    if (!canvas) return;

    // Si ya está inicializado, no hacemos nada
    if (canvas.getAttribute('data-initialized') === 'true') return;
    canvas.setAttribute('data-initialized', 'true');

    const ctx = canvas.getContext('2d');
    let width = window.innerWidth;
    let height = window.innerHeight;

    canvas.width = width;
    canvas.height = height;

    const fontSize = 14;
    const columns = Math.floor(width / fontSize);
    const drops = [];
    for (let x = 0; x < columns; x++) drops[x] = 1;

    const binary = "10";

    const draw = () => {
        // Si el canvas ya no está en el documento, paramos la animación
        if (!document.body.contains(canvas)) return;

        ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
        ctx.fillRect(0, 0, width, height);
        ctx.fillStyle = "#00BFFF";
        ctx.font = fontSize + "px monospace";



        for (let i = 0; i < drops.length; i++) {
            const text = binary.charAt(Math.floor(Math.random() * binary.length));
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
        requestAnimationFrame(draw);
    };
    draw();

    const handleResize = () => {
        if (!document.body.contains(canvas)) {
            window.removeEventListener('resize', handleResize);
            return;
        }
        width = window.innerWidth;
        height = window.innerHeight;

        canvas.width = width;
        canvas.height = height;
        const newColumns = Math.floor(width / fontSize);
        for (let x = drops.length; x < newColumns; x++) drops[x] = 1;
    };

    window.addEventListener('resize', handleResize);
};


// Comprobamos periódicamente si el canvas necesita reinicializarse
setInterval(initMatrix, 100);
"""


def pagina_principal() -> rx.Component:
    return rx.box(
        rx.script(matrix_js),
        rx.html('<canvas id="matrix-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;"></canvas>'),
        rx.box(
            index(),
            position="relative",
            z_index="1",
            background="rgba(0, 0, 0, 0.3)",
            width="100%",
            padding=rx.breakpoints(initial="1em", sm="1.5em",
                                   md="2em", lg="2.5em", xl="3em"),
        ),
        width="100vw",
        min_height="155vh",
    )


app = rx.App(stylesheets=["/custom.css"])
app.add_page(pagina_principal, route="/")
