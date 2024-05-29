import os
import msvcrt
os.system("cls")

users = {"nombre": "", "contrasena": ""}

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

    elif opc == 3:
        print("Eliminar usuario.\n")
        eliminar = input("Ingrese nombre de usuario a eliminar: ")
    else:
        print("Usted ha salido con éxito...")
        break
