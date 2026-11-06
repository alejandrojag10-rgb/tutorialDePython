#Tutorial de Fundamentos de Python - Parte 2: Estructuras de Control, Funciones y Módulos

import math
import random


# ==========================================
# 1. FLUJO DE CONTROL (if, elif, else)
# ==========================================
# Las estructuras de control dirigen la ejecución según condiciones booleanas.
print("--- 1. Flujo de Control ---")

promedio_notas = 4.2
estrato_socioeconomico = 2

# Lógica condicional evaluada de arriba a abajo
if promedio_notas > 4.8:
    print("Estado: ¡Beca del 100% concedida!")
elif promedio_notas >= 4.0 and estrato_socioeconomico < 3:
    print("Estado: ¡Beca parcial del 50% concedida!")
else:
    print("Estado: Tarifa de matrícula estándar")
print()


# ==========================================
# 2. BUCLES E ITERACIÓN
# ==========================================
print("--- 2. Bucles e Iteración ---")

# Bucle FOR estándar sobre una lista
estudiantes = ["Ana", "Carlos", "María"]
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante}")
print()

# range(inicio, fin_no_incluido, paso) genera una secuencia de números
print("Conteo usando range():")
for i in range(1, 4):
    print(f"  Paso #{i}")
print()

# enumerate() devuelve tanto el índice (empezando en 0 o personalizado) como el elemento
print("Lista numerada con enumerate():")
for indice, estudiante in enumerate(estudiantes, start=1):
    print(f"  {indice}. {estudiante}")
print()

# zip() itera sobre dos o más listas en paralelo
programas = ["Economía", "Ingeniería", "Derecho"]
print("Iteración en paralelo con zip():")
for estudiante, programa in zip(estudiantes, programas):
    print(f"  {estudiante} estudia {programa}")
print()


# ==========================================
# 3. COMPRENSIÓN DE LISTAS Y DICCIONARIOS
# ==========================================
# Sintaxis compacta para transformar o filtrar iterables en nuevas colecciones.
print("--- 3. Comprensión de Listas y Diccionarios ---")

notas = [3.5, 4.3, 2.5, 1.5, 4.9, 3.7]

# Filtrar elementos de una lista con un 'if' al final
notas_aprobatorias = [n for n in notas if n >= 3.0]
print("Notas aprobatorias (>= 3.0):", notas_aprobatorias)

# Transformar elementos condicionalmente usando 'if-else'
etiquetas_estado = ["Aprobado" if n >= 3.0 else "Reprobado" for n in notas]
print("Etiquetas de estado:", etiquetas_estado)

# Comprensión de diccionarios relacionando elementos con valores calculados
calificaciones_estudiantes = {"Ana": 4.5, "Carlos": 2.8, "María": 3.9}
estudiantes_evaluados = {
    nombre: "Aprobado" if nota >= 3.0 else "Reprobado"
    for nombre, nota in calificaciones_estudiantes.items()
}
print("Diccionario evaluado:", estudiantes_evaluados)
print()


# ==========================================
# 4. FUNCIONES Y BUENAS PRÁCTICAS
# ==========================================
# Las funciones empaquetan bloques de código reutilizables.
# Las buenas prácticas incluyen Pistas de Tipo (Type Hints) y Docstrings (documentación).
print("--- 4. Funciones ---")


def calcular_salario(horas_trabajadas: int, tarifa_hora: float = 25.0) -> float:
    """Calcula el salario total basado en las horas trabajadas y la tarifa por hora.

    Args:
        horas_trabajadas (int): Número de horas trabajadas.
        tarifa_hora (float): Tarifa cobrada por hora. Valor por defecto: 25.0.

    Returns:
        float: Salario total calculated.
    """
    return horas_trabajadas * tarifa_hora


def analizar_texto(texto: str) -> dict:
    """Tokeniza el texto y clasifica las palabras según su tipo.

    Args:
        texto (str): Cadena de texto de entrada.

    Returns:
        dict: Resumen con el recuento de tipos de palabras.
    """
    palabras = texto.split()
    recuento_numerico = sum(1 for p in palabras if p.isnumeric())
    recuento_alfabetico = sum(1 for p in palabras if p.isalpha())
    return {
        "total_palabras": len(palabras),
        "numericas": recuento_numerico,
        "alfabeticas": recuento_alfabetico,
    }


# Llamada a funciones usando argumentos con nombre
pago = calcular_salario(horas_trabajadas=40, tarifa_hora=30.0)
print(f"Pago calculado: ${pago:.2f}")

info_texto = analizar_texto("hoy es 16 de marzo del ano 2026")
print("Resultado del análisis de texto:", info_texto)
print()


# ==========================================
# 5. MÓDULOS Y LIBRERÍAS ESTÁNDAR
# ==========================================
# Los módulos permiten reutilizar funciones de la librería estándar o archivos externos.
print("--- 5. Módulos Estándar ---")

# Uso de funciones del módulo math
numero = 16
raiz_cuadrada = math.sqrt(numero)
factorial = math.factorial(5)
print(f"Raíz cuadrada de {numero}: {raiz_cuadrada}")
print(f"Factorial de 5: {factorial}")

# Uso del módulo random
estudiante_aleatorio = random.choice(estudiantes)
print(f"Estudiante seleccionado aleatoriamente: {estudiante_aleatorio}")