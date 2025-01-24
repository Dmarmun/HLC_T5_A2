import random
def numero():
    numero_secreto= random.randint(1, 50)
    adivinado= False
    print("Adivina el número (entre 1 y 50):")
    while not adivinado:
        intento= int(input("Tu intento: "))
        if intento < numero_secreto:
            print("Más alto.")
        elif intento > numero_secreto:
            print("Más bajo.")
        else:
            print("¡Correcto!")
            adivinado= True
numero()