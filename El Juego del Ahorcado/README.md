# 🎯 El Juego del Ahorcado

Un juego del ahorcado desarrollado en Python con arquitectura modular, base de datos de palabras y soporte para asistencia por IA.

# 📁 Estructura del Proyecto

```
El Juego del Ahorcado/
├── data/                      # Datos del juego (palabras, categorías, etc.)
├── docs/
│   └── asistecia_ia.md        # Documentación sobre la asistencia por IA
├── src/
│   ├── __init__.py
│   ├── database.py            # Gestión de la base de datos de palabras
│   ├── logic.py               # Lógica principal del juego
│   ├── main.py                # Punto de entrada de la aplicación
│   └── visual.py              # Interfaz visual / renderizado
├── test/
│   └── src/
│       ├── __init__.py
│       ├── test_database.py   # Tests para el módulo de base de datos
│       ├── test_logic.py      # Tests para la lógica del juego
│       ├── test_main.py       # Tests del flujo principal
│       └── test_visual.py     # Tests de la interfaz visual
├── __init__.py
├── .gitignore
├── LICENSE
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