#Tutorial de Fundamentos de Python - Parte 1


# 1. TIPOS DE DATOS BÁSICOS Y VARIABLES
# Los tipos comunes de variables incluyen enteros (números enteros), flotantes (decimales),
# cadenas de texto (str) y booleanos (verdadero/falso).

edad_usuario = 25              # Entero (int)
saldo_cuenta = 150.75          # Número de punto flotante (float)
nombre_usuario = "Daniel"        # Cadena de texto (str)
es_miembro_activo = True       # Booleano (bool)

# Usamos print() y type() para inspeccionar valores y tipos de datos
print("--- 1. Tipos de datos ---")
print("Nombre de usuario:", nombre_usuario)
print("Tipo de dato de edad:", type(edad_usuario))
print("Tipo de dato de saldo:", type(saldo_cuenta))
print()


# ==========================================
# 2. OPERACIONES Y CADENAS F (F-STRINGS)
# ==========================================
print("--- 2. Operaciones y F-Strings ---")

# Operaciones numéricas
edad_siguiente_ano = edad_usuario + 1
saldo_actualizado = saldo_cuenta - 20.0

# Operaciones de comparación / lógicas (devuelven verdadero o falso)
es_mayor_edad = edad_usuario >= 18
tiene_fondos = saldo_cuenta > 0
puede_comprar = es_mayor_edad and tiene_fondos  # Combinación lógica

# Formato de cadenas con f-strings (inserta variables directamente entre {})
print(f"¡Hola, {nombre_usuario}!")
print(f"El próximo año tendrás {edad_siguiente_ano} años.")
print(f"Saldo actualizado: ${saldo_actualizado:.2f}")
print(f"¿Elegible para compras? {puede_comprar}")
print()


# ==========================================
# 3. MÉTODOS ÚTILES PARA CADENAS DE TEXTO
# ==========================================
# Las cadenas de texto tienen funciones incorporadas (métodos) para manipularlas.
print("--- 3. Métodos de cadenas de texto ---")

mensaje = "  hola mundo  "

# Transformar texto
print("Mayúsculas:", mensaje.upper())             # Convierte todo a mayúsculas
print("Formato Título:", mensaje.title())          # Convierte en mayúscula la primera letra de cada palabra
print("Texto limpio:", mensaje.strip())            # Elimina espacios en blanco alrededor
print("Texto reemplazado:", mensaje.replace("mundo", "Python"))  # Reemplaza palabras
print()


# ==========================================
# 4. ESTRUCTURAS DE DATOS FUNDAMENTALES
# ==========================================
# Las estructuras de datos permiten agrupar múltiples elementos en una sola variable.
print("--- 4. Estructuras de datos ---")

# TUPLAS: Inmutables (no se pueden modificar tras crearse), ordenadas.
coordenadas_fijas = (10, 20)
print("Tupla:", coordenadas_fijas)

# LISTAS: Mutables (se pueden añadir, eliminar o modificar elementos), ordenadas.
frutas = ["manzana", "banano", "cereza"]
frutas.append("naranja")       # Añade un elemento al final
frutas.remove("banano")        # Elimina un elemento específico
print("Lista tras modificaciones:", frutas)

# CONJUNTOS (SETS): Mutables, DESORDENADOS y almacenan elementos ÚNICOS (elimina duplicados).
etiquetas = {"python", "código", "python", "principiante"}  # "python" está duplicado
print("Conjunto (elimina duplicados automáticamente):", etiquetas)

# DICCIONARIOS: Almacenan datos en pares Clave-Valor.
estudiante = {
    "nombre": "María",
    "edad": 22,
    "cursos": ["Matemáticas", "Informática"]
}
estudiante["nota"] = "A"       # Añade un nuevo par clave-valor
print("Diccionario:", estudiante)
print()


# ==========================================
# 5. INDEXACIÓN Y REBANADO (SLICING)
# ==========================================
# Las colecciones ordenadas (Listas, Tuplas) usan indexación basada en cero (empieza en 0).
print("--- 5. Indexación y Slicing ---")

numeros = [10, 20, 30, 40, 50]

# Acceso a elementos individuales
print("Primer elemento (índice 0):", numeros[0])
print("Último elemento (índice -1):", numeros[-1])

# Sintaxis de rebanado (slicing): lista[inicio : fin_no_incluido]
print("Primeros dos elementos (índices 0 y 1):", numeros[0:2])
print("Desde el índice 2 hasta el final:", numeros[2:])

# Acceso a valores en diccionarios mediante sus claves (en lugar de índices numéricos)
print("Nombre del estudiante desde dict:", estudiante["nombre"])