import sqlite3

# Conexión a la base de datos (creará un archivo "mi_base_de_datos.db" si no existe)
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Consulta SQL para crear una tabla llamada "usuarios"
crear_tabla_sql = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    edad INTEGER
)
"""
insertar_sql="""
    INSERT INTO usuarios(nombre,email,edad)values("Guillermo Alvarez",20,"ventiventixx@gmail.com")
"""

# Ejecutar la consulta para crear la tabla
cursor.execute(crear_tabla_sql)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
