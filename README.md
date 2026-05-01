# 🚀 Portafolio Profesional | Pedro Pérez

Bienvenido al repositorio de mi portafolio personal. Como **Analista de Sistemas** enfocado en el desarrollo de software y arquitectura lógica, este proyecto demuestra mi capacidad para construir aplicaciones web modernas, interactivas y escalables utilizando únicamente **Python** mediante el framework **Reflex**.

## 🚀 Tecnologías Utilizadas

*   **Framework Principal:** [Reflex](https://reflex.dev/) (Full-stack Python)
*   **Diseño Visual:** Estética *Glassmorphism* con filtros de desenfoque y transparencias.
*   **Interactividad:** Inyección de JavaScript personalizado para el efecto visual "Matrix Canvas".
*   **Optimización:** Diseño 100% responsivo ajustado para móviles, tablets y desktops.

## ✨ Características Destacadas

*   **Arquitectura MVC:** Separación clara entre lógica de estado (`ProyectosState`), estilos globales y componentes reutilizables.
*   **Carga Dinámica:** Sistema automatizado de detección de capturas de pantalla para la galería de proyectos mediante el escaneo de directorios.
*   **Seguridad:** Implementación de variables de entorno mediante `.env` para proteger datos de contacto sensibles.
*   **Experiencia de Usuario:** Transiciones suaves, sombras dinámicas y modales integrados para la visualización de trabajos.

## 📋 Requisitos

*   **Python:** 3.10 o superior.
*   **Reflex:** v0.8.27.
*   **Variables de entorno:** Dependencia de `python-dotenv`.

## 📂 Estructura del Proyecto

```text
pagina_web/
├── assets/             # Recursos estáticos (Imágenes, iconos, custom.css)
├── pagina_web/
│   ├── componentes.py  # Componentes UI reutilizables (Nav, Footer, Matrix)
│   ├── pagina_web.py   # Definición de rutas, vistas y estados de la app
│   └── styles.py       # Configuración global de estilos, fuentes y datos
├── .env                # Configuración de variables sensibles (No trackeado en Git)
├── README.md           # Documentación del proyecto
└── requirements.txt    # Dependencias de Python necesarias
```

## 🛠️ Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/pedrodanielpereztorres-maker/tu-repositorio.git
    cd tu-repositorio
    ```

2.  **Crear y activar un entorno virtual (Recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar variables de entorno:**
    Crea un archivo llamado `.env` en la carpeta raíz y define tus datos:
    ```env
    PHONE_NUMBER=584245671687
    EMAIL_ADDRESS=pedrodanielpereztorres@gmail.com
    GITHUB_USER=pedrodanielpereztorres-maker
    ```

## 🏃 Ejecución

Para iniciar el entorno de desarrollo local:
```bash
reflex run
```