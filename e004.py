def check_pass():
    system_pass= "Simire2"
    tries= 0
    while tries<3:
        user_pass= input("Introduce la contraseña: (La contraseña es Simrie2)")
        if user_pass== system_pass:
            print("Bienvenido")
            break
        else:
            print("Contraseña incorrecta")
            tries+= 1