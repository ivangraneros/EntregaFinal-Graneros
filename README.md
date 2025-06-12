# EntregaFinal-Graneros

- /inicio/ es la pagina principal

# Proyecto Final: Playground Blog

Este es un proyecto individual desarrollado como entrega final del curso. Se trata de una aplicación web estilo blog creada con Django, que permite a los usuarios registrarse, iniciar sesión, gestionar su perfil y publicar páginas con contenido enriquecido.

## 🛠 Tecnologías utilizadas

- Python 3
- Django 4.x
- HTML5 / CSS3
- Bootstrap
- SQLite (base de datos por defecto)
- Templates con herencia
- CBV (Class Based Views)
- Formularios personalizados

## ✨ Funcionalidades

- Registro de usuarios
- Inicio de sesión y cierre de sesión
- Vista de perfil con edición y cambio de contraseña
- Publicación de páginas (con título, subtítulo, contenido, imagen y fecha)
- CRUD completo de páginas (solo para usuarios logueados)
- Vista "Acerca de mí"
- Navegación clara y estructurada (NavBar)
- Mensajes de aviso si no hay páginas aún
- Imagen de perfil, biografía y fecha de nacimiento
- Sistema de mensajeria dentro de la APP

## 📂 Estructura principal

```bash
blog/             # Proyecto principal
│
├── PaginaWeb/    # App principal
│   ├── templates/
│   │   ├── base.html
│   │   └── pages/
│   │       ├── page_list.html
│   │       ├── page_detail.html
│   │       ├── about.html
│   │       └── ...
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── static/
├── media/
├── requirements.txt
├── .gitignore
└── README.md
