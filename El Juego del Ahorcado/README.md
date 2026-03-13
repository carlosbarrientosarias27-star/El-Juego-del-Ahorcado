# 🎯 El Juego del Ahorcado

Un juego del ahorcado desarrollado en Python con arquitectura modular, base de datos de palabras y soporte para asistencia por IA.

# 📁 Estructura del Proyecto

```
├── data/
│   └── palabras.db               # Base de datos con las palabras del juego
│
└── El Juego del Ahorcado/
    ├── database/
    │   ├── __init__.py
    │   └── db_handler.py             # Gestión y acceso a la base de datos
    ├── docs/
    │   └── asistecia_ia.md           # Documentación de asistencia con IA
    ├── logic/
    │   ├── __init__.py
    │   ├── game_engine.py            # Motor principal del juego
    │   └── validators.py             # Validaciones de entrada y lógica
    ├── tests/
    │   ├── database/
    │   │   ├── __init__.py
    │   │   └── test-db_handler.py    # Tests del manejador de base de datos
    │   ├── logic/
    │   │   ├── __init__.py
    │   │   ├── tests-game_engine.py  # Tests del motor de juego
    │   │   └── tests-validators.py   # Tests de validaciones
    │   ├── ui/
    │   │   ├── __init__.py
    │   │   └── tests_visuals.py      # Tests de la interfaz visual
    │   ├── __init__.py
    │   └── test_main.py              # Tests del punto de entrada principal
    ├── ui/
    │   ├── __init__.py               # Módulo de interfaz de usuario
    │   └── visuals.py                # Componentes visuales de la interfaz
    ├── __init__.py
    ├── .gitignore
    ├── LICENSE
    ├── main.py                       # Punto de entrada principal
    ├── README.md
    └── requirements.txt
```

# 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd El-Juego-del-Ahorcado
   ```


# 🎮 Uso

Ejecuta el juego desde la raíz del proyecto:

```
python src/main.py
```

# 🧩 Módulos

| Módulo | Descripción |
|--------|-------------|
| `database.py` | Carga y gestiona el banco de palabras del juego |
| `logic.py` | Controla el estado del juego, turnos y condiciones de victoria/derrota |
| `visual.py` | Renderiza la interfaz del ahorcado y el estado de la palabra |
| `main.py` | Inicializa y orquesta todos los módulos |

# 🤖 Asistencia por IA

Este proyecto incluye soporte para asistencia mediante inteligencia artificial. Consulta [`docs/asistecia_ia.md`](docs/asistecia_ia.md) para más detalles sobre su implementación y uso.

# 🧪 Tests

Ejecuta la suite de pruebas con:

```
python -m pytest test/
```

O prueba un módulo específico:

```
python -m pytest test/src/test_logic.py
```

# 📄 Licencia

Este proyecto está bajo los términos de la licencia incluida en el archivo [LICENSE](LICENSE MIT).