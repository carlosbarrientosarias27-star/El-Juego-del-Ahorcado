# 1. Documentación de Asistencia IA (asistecia_ia.md)
Dado que estás usando herramientas de IA, este archivo debería servir como un diario de prompts y decisiones. 

- Te sugiero incluir:Contexto del Modelo: Qué IA usaste y para qué tareas específicas (ej. "Generación de tests unitarios con Gemini").

- Registro de Prompts: Copia y pega los prompts que mejor resultado te dieron para la lógica del juego.

- Lecciones Aprendidas: Errores que la IA cometió (como bucles infinitos en la entrada de datos) y cómo los corregiste.

# 2. Refactorización del Código
Tu estructura actual sugiere un patrón modular. Aquí te detallo qué revisar en cada archivo para hacerlo más robusto:

## logic.py (El cerebro)

- Desacoplamiento: Asegúrate de que no haya print() ni input() aquí. Esta capa solo debe procesar datos (verificar si una letra está en la palabra, actualizar el estado del ahorcado).

- Estado: Usa una clase GameSession para manejar el estado en lugar de variables globales.

## visual.py (La interfaz)

- Flexibilidad: Haz que las funciones reciban el número de errores y devuelvan el "dibujo" correspondiente o lo impriman.

- Limpieza: Añade una función para limpiar la consola según el sistema operativo.

## database.py (Persistencia)

- Manejo de Errores: Usa bloques try-except para leer el archivo de palabras. Si el archivo no existe, debe cargar una lista de palabras por defecto para que el juego no se rompa.

# 3. Pruebas de Casos Borde (Edge Cases)
Tus archivos en la carpeta test/src/ deben validar situaciones "extrañas" que un usuario podría provocar. Enfócate en estos escenarios. Para asegurar la robustez del juego, se han definido los siguientes escenarios de prueba:

| Componente | Caso Borde a Probar | Resultado Esperado |
| :--- | :--- | :--- |
| **Entrada de Usuario** | Ingreso de números, símbolos o espacios vacíos. | El sistema debe ignorar la entrada y solicitar una letra válida (A-Z). |
| **Tratamiento de Palabras** | Palabras con tildes (á, é...), espacios o guiones. | Normalización de caracteres (ej. 'á' -> 'a') para evitar dificultades injustas. |
| **Lógica de Repetición** | Ingresar la misma letra (correcta o incorrecta) varias veces. | No debe restar vidas adicionales ni contar como un intento nuevo. |
| **Condiciones de Fin** | Ganar o perder en el límite exacto de intentos. | El juego debe finalizar limpiamente, mostrando el mensaje pertinente y liberando recursos. |