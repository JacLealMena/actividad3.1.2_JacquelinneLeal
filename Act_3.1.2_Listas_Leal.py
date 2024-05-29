import os
import msvcrt
os.system("cls")

users = []
contrasenas = []

while True:
    print("""
Menú

1. Inicio sesión.
2. Registrar usuario.
3. Eliminar usuario.
4. Salir.
""")
    opc = int(input("Opción: "))
    if opc == 1:
        pass
    elif opc == 2:
        nombre = input("Nombre de usuario: ")
        contra = input("Contraseña: ")
        users.append(nombre)
        contrasenas.append(contra)
    elif opc == 3:
        pass
    else:
        pass
