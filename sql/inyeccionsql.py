import sqlite3

def autenticar_usuario_vulnerable(cursor, usuario):
    consulta = "SELECT * FROM usuarios WHERE email = '" + usuario + "'"
    cursor.execute(consulta)
    return cursor.fetchone() is not None

# Conexión a la base de datos (creará un archivo "usuarios.db" si no existe)
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

while True:
    print("Bienvenido! Ingrese su correo electrónico:")
    usuario = input("Correo electrónico: ")

    if autenticar_usuario_vulnerable(cursor, usuario):
        print("Autenticación exitosa. ¡Bienvenido!")
        break
    else:
        print("Correo electrónico incorrecto. Inténtalo nuevamente.")

# Cerrar la conexión a la base de datos
conn.close()
