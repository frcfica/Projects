import sqlite3

# 1. Conectar a la base de datos (si el archivo no existe, se creará automáticamente)
conexion = sqlite3.connect("mi_base_de_datos.db")

# 2. Crear un objeto cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# 3. Crear una tabla (si no existe ya)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER
    )
"""
)
print("¡Tabla creada con éxito!")

# 4. Insertar datos (Cuidado: usamos '?' para evitar inyección SQL)
nombre_usuario = "Carlos"
edad_usuario = 28

cursor.execute(
    "INSERT INTO usuarios (nombre, edad) VALUES (?, ?)",
    (nombre_usuario, edad_usuario),
)
# Es obligatorio hacer .commit() para guardar los cambios en la base de datos
conexion.commit()
print(f"Usuario {nombre_usuario} insertado correctamente.")

# 5. Consultar los datos (SQL Select)
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()  # Recupera todos los resultados

print("\n--- Lista de Usuarios en la Base de Datos ---")
for usuario in usuarios:
    # usuario[0] es el id, usuario[1] el nombre, usuario[2] la edad
    print(f"ID: {usuario[0]} | Nombre: {usuario[1]} | Edad: {usuario[2]}")

# 6. Cerrar la conexión siempre al terminar
conexion.close()