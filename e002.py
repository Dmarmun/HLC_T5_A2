n1=int(input("Introduce el primer número: "))
n2=int(input("Introduce el segundo número: "))
n3=int(input("Introduce el tercer número: "))
if (n1==n2 and n2==n3):
    print("Todos los número son iguales.")
elif (n1==n2):
    print("Los dos primeros número son iguales.")
elif (n2==n3):
    print("Los dos últimos número son iguales.")
elif (n1==n3):
    print("El primer y el último número son iguales.")
elif (n1>n2 and n1>n3):
    print("El primer número es el mayor.")
elif (n2>n1 and n2>n3):
    print("El segundo número es el mayor.")
else:
    print("El tercer número es el mayor.")