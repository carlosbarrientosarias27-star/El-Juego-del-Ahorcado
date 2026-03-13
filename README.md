# 🎮 El Juego del Ahorcado

Juego clásico del Ahorcado desarrollado en Python, con arquitectura modular que separa la lógica, base de datos e interfaz visual. Incluye además un **Proyecto de Prueba** como entorno de experimentación simplificado.

---

# 📁 Estructura General

```
├── El Juego del Ahorcado/
│   ├── database/
│   │   └── db_handler.py          # Gestión y acceso a la base de datos
│   ├── docs/
│   │   └── asistecia_ia.md        # Documentación de asistencia con IA
│   ├── logic/
│   │   ├── __init__.py
│   │   ├── game_engine.py         # Motor principal del juego
│   │   └── validators.py          # Validaciones de entrada y lógica
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_main.py           # Tests del punto de entrada principal
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   └── test-db_handler.py
│   │   ├── logic/
│   │   │   ├── __init__.py
│   │   │   ├── tests-game-engine.py
│   │   │   └── tests-validators.py
│   │   └── ui/
│   │       ├── __init__.py
│   │       └── tests_visuals.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── visuals.py             # Componentes visuales de la interfaz
│   ├── __init__.py
│   ├── .gitignore
│   ├── LICENSE
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
│
└── Proyecto de Prueba/
    ├── __init__.py
    ├── Juego de Ahorcado.py       # Implementación simplificada del juego
    └── Readme.md
```

---

# 🚀 El Juego del Ahorcado

## Instalación

1. **Clona el repositorio:**
   ```
   git clone <url-del-repositorio>
   cd "El Juego del Ahorcado"
   ```

2. **Ejecuta el juego:**
   ```
   python main.py
   ```

## Módulos

| Módulo | Descripción |
|--------|-------------|
| `database/db_handler.py` | Gestiona la conexión a la base de datos: carga de palabras, puntuaciones y estadísticas |
| `logic/game_engine.py` | Motor principal: flujo de partida, turnos, intentos y condición de victoria/derrota |
| `logic/validators.py` | Valida entradas del usuario: letras válidas, repetidas y reglas del juego |
| `ui/` | Interfaz visual: renderizado del ahorcado, estado de la palabra y mensajes |

## Tests

```
# Ejecutar todos los tests
python -m pytest tests/

# Tests por módulo específico
python -m pytest tests/logic/
python -m pytest tests/database/
python -m pytest tests/ui/
```

---

# 🧪 Proyecto de Prueba

Entorno aislado para experimentar con la lógica del juego de forma rápida y sin dependencias adicionales.

## Uso

```
cd "Proyecto de Prueba"
python "Juego de Ahorcado.py"
```

## Propósito

- Probar nuevas funcionalidades antes de integrarlas al proyecto principal.
- Realizar demostraciones rápidas del funcionamiento básico.
- Servir como referencia de implementación simplificada.

---

# 🔍 Comparativa entre proyectos

| Característica         | El Juego del Ahorcado | Proyecto de Prueba |
|------------------------|:---------------------:|:------------------:|
| Arquitectura modular   | ✅                    | ❌                 |
| Base de datos          | ✅                    | ❌                 |
| Suite de tests         | ✅                    | ❌                 |
| Lógica del juego       | ✅                    | ✅                 |
| Fácil ejecución        | ⚙️                    | ✅                 |

> El **Proyecto de Prueba** no está pensado para producción. Para la versión completa y estable, usar el proyecto principal.

---

# 📄 Licencia

Este proyecto está bajo los términos descritos en el archivo [LICENSE](El%20Juego%20del%20Ahorcado/LICENSE MIT).
