import random

x = int(random.randint(1,10))
y = True
print("se ha generado un numero al azar del 1 al 10, trate de adivina.")
while y:
    
    z = int(input("Ingresar numero: "))
    if (z == x):
        y = False
        print("Has adivinado el numero!!!!!")
        break
    elif (z < x):
        print("El numero que ingreso es menor al numero generado.\n\nIntente de nuevo!\n")
        y = True
        continue
    
    elif (z > x):
        print("El numero que ingreso es mayor al numero generado.\n\nIntente de nuevo!\n")
        y = True
        continue
        
