# 🐾 VetCitas — Sistema de Gestión de Citas Veterinarias

Aplicación web para la gestión de citas en una clínica veterinaria, desarrollada con **Flask**, **SQLite** y **Bootstrap 5**.

## 📋 Funcionalidades

- **Agenda**: Visualización de todas las citas programadas en tarjetas (Cards).
- **Agendar**: Formulario para registrar una nueva cita médica.
- **Modificar**: Edición de los datos o la fecha de una cita existente.
- **Cancelar**: Eliminación de una cita del sistema.

## 🛠️ Tecnologías

| Tecnología   | Uso                          |
|-------------|------------------------------|
| Python 3    | Lenguaje backend             |
| Flask       | Microframework web           |
| SQLite      | Base de datos relacional     |
| Jinja2      | Motor de plantillas          |
| Bootstrap 5 | Framework CSS para frontend  |
| Git/GitHub  | Control de versiones         |

## 🚀 Instalación y Ejecución

```bash
# 1. Clonar el repositorio
git clone https://github.com/Ale-72/Sistema-de-citas-medicas-Examen
cd Sistema-de-citas-medicas-Examen

# 2. Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000`

## 📁 Estructura del Proyecto

```
Examen/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── .gitignore            # Archivos ignorados por Git
├── README.md             # Documentación del proyecto
├── static/
│   └── estilos.css       # Estilos personalizados
└── templates/
    ├── base.html         # Plantilla base (herencia)
    ├── agenda.html       # Vista de la agenda
    ├── agendar.html      # Formulario nueva cita
    └── modificar.html    # Formulario editar cita
```

## 📊 Base de Datos

Base de datos SQLite (`citas.db`) con la tabla **pacientes**:

| Campo        | Tipo    | Descripción                          |
|-------------|---------|--------------------------------------|
| id          | INTEGER | Clave primaria, autoincrementable    |
| mascota     | TEXT    | Nombre de la mascota (obligatorio)   |
| propietario | TEXT    | Nombre del propietario (obligatorio) |
| especie     | TEXT    | Especie del animal                   |
| fecha       | TEXT    | Fecha de la cita (obligatorio)       |
