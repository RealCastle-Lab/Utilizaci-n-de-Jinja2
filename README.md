# Aplicación Web de Datos de Vacunación con Flask y Redis

## Descripción del Proyecto
Esta aplicación web proporciona acceso a los datos de vacunación contra el sarampión en niños entre 12-23 meses en Panamá. Utilizando Flask y Redis, la aplicación ofrece una interfaz web interactiva que permite a los usuarios consultar y visualizar datos históricos de vacunación a través de una interfaz web desarrollada con el motor de plantillas Jinja2.

## Características
- **Visualización de Datos**: Muestra todos los registros de vacunación almacenados en Redis en la página principal.
- **Consulta de Datos por Año**: Permite a los usuarios buscar registros específicos por año.
- **Página Acerca de**: Proporciona información sobre la aplicación, sus objetivos y las tecnologías utilizadas.

## Tecnologías Utilizadas
- **Flask**: Un microframework de Python para construir aplicaciones web.
- **Redis**: Una base de datos en memoria usada para almacenar los datos de vacunación.
- **Jinja2**: Un potente motor de plantillas para Python que se utiliza para renderizar las vistas HTML.

## Estructura del Proyecto
```plaintext
redis_web_app/
│
├── app/
│   ├── __init__.py        # Configura e inicializa la aplicación Flask
│   ├── routes.py          # Define las rutas de la aplicación
│   ├── templates/         # Contiene archivos HTML para Jinja2
│   │   ├── layout.html    # Plantilla base
│   │   ├── index.html     # Vista principal
│   │   └── about.html     # Vista de la página Acerca de
│   └── static/            # Almacena archivos CSS y JavaScript
│
├── tests/
│   ├── test_app.py        # Pruebas unitarias para la aplicación Flask
│
├── requirements.txt       # Dependencias del proyecto
├── .gitignore             # Especifica los archivos no rastreados por Git
└── README.md              # Documentación del proyecto
