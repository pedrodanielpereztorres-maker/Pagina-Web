import os
import reflex as rx
from dotenv import load_dotenv

load_dotenv()

# --- DATOS DE CONTACTO (Desde .env) ---
PHONE_NUMBER = os.getenv("PHONE_NUMBER", "584245671687")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", "tu-correo@gmail.com")
GITHUB_USER = os.getenv("GITHUB_USER", "tu-usuario-github")

# --- CONFIGURACIÓN VISUAL ---
COLOR_ACCION = "#00BFFF"  # Deep Sky Blue para resaltar
FONDO_TARJETA = "rgba(255, 255, 255, 0.03)"
TEXTO_SECUNDARIO = "#E0E0E0"
BORDE_FINO = "1px solid rgba(255, 255, 255, 0.1)"

# Fuentes tipográficas
FUENTE_TITULOS = "Cinzel, serif"
FUENTE_CUERPO = "Raleway, sans-serif"

# Tamaños para títulos grandes (Hero)
TAMANIO_TITULO_HERO = rx.breakpoints(
    initial="2.2em", sm="5em", md="7em", lg="9em", xl="10em"
)

# Tamaños para subtítulos
TAMANIO_SUBTITULO = rx.breakpoints(
    initial="1.15em", sm="1.8em", md="2.8em", lg="3.5em", xl="4em"
)

# Tamaños para títulos de sección (Sobre Mí, Proyectos, Lenguajes)
TAMANIO_TITULO_SECCION = rx.breakpoints(
    initial="1.6em", sm="2.2em", md="2.8em", lg="3.2em"
)

# Tamaños adaptables para el texto de descripción
TEXTO_RESPONSIVO = rx.breakpoints(
    initial="1em", sm="1.4em", md="1.5em", lg="1.6em", xl="1.8em"
)

# Espaciado superior estándar para que el menú fijo no tape el contenido
ESPACIADO_TOP_PAGINA = rx.breakpoints(initial="120px", sm="150px", lg="200px")

# Espaciados de letras adaptables
LETTER_SPACING_HERO = rx.breakpoints(initial="2px", sm="5px")
LETTER_SPACING_SUB = rx.breakpoints(initial="1px", sm="3px")

# --- CARGA DINÁMICA DE IMÁGENES ---
def obtener_imagenes_proyecto(carpeta: str) -> list[str]:
    """Escanea la carpeta en assets/projects/{carpeta} y devuelve las rutas de las imágenes."""
    ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_abs = os.path.join(ruta_base, "assets", "projects", carpeta)
    
    if not os.path.exists(ruta_abs):
        return []
    
    # Extensiones de imagen soportadas
    extensiones = (".png", ".jpg", ".jpeg", ".webp")
    archivos = [
        f"/projects/{carpeta}/{f}" 
        for f in os.listdir(ruta_abs) 
        if f.lower().endswith(extensiones)
    ]
    return sorted(archivos) # Ordenadas alfabéticamente

# --- DATOS DE LA WEB ---
IMGS_CDI = obtener_imagenes_proyecto("cdi")
IMGS_TESIS = obtener_imagenes_proyecto("sistema_tesis")

DATOS_PROYECTOS = [
    {
        "titulo": "Sistema de Tesis", 
        "desc": "Sistema de gestión de tesis desarrollado para la Universidad IUTEPI para la mejora de la administracion de trabajo de grado.", 
        "img": "/projects/sistema_tesis/login.jpeg", 
        "imagenes": IMGS_TESIS,
        "url": "#",
        "lenguaje": "Python",
        "framework": "Reflex",
        "bd": "PostgreSQL"
    },
    {
        "titulo": "Sistema de Inventario", 
        "desc": "Sistema integral de gestión y control de inventarios desarrollado para el CDI Campo Lindo.", 
        "img":"/projects/cdi/login.png", 
        "imagenes": IMGS_CDI,
        "url": "#",
        "lenguaje": "Python",
        "framework": "Reflex",
        "bd": "PostgreSQL"
    },
    
]

DATOS_LENGUAJES = [
    {"src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/visualbasic/visualbasic-original.svg", "alt": "VBA"},
    {"src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg", "alt": "C++"},
    {"src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg", "alt": "Python"},
    {"src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg", "alt": "SQL"},
    {"src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg", "alt": "NoSQL"},
    {"src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg", "alt": "JavaScript"},
    {"src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg", "alt": "Git"},
    {"src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg", "alt": "HTML5"},
    {"src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg", "alt": "CSS3"},
    {"src": "/favicon.ico", "alt": "Reflex"},
]