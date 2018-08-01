'''Crear una función que como resultado de el factorial de un número.

Crear una función que imprima la serie fibonacci.
	·Debe recibir como parámetro la cantidad de números de la serie.
	
Crear una función que calcule el múltiplo de 3.
	·Recibe un número y te devuelve la multiplicación.
	(Ejemplo: Si recibe '9' regresa 27)
	
Crear una función que imprima el triángulo de Pascal (este ejercicio no es igual que el de la matriz de 6x6, pero sirve como base para él).'''
def factorial(x):
    if x == 0:
        return 1

    else:
        return (x * factorial(x-1))

def fibo(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return (fibo(x-1) + fibo(x-2))

def multi(x,y):
    if y == 0:
        return x
    else:
        return (x + multi(x,y-1))

def pascal(x): 
    if x == 1: 
        return [[1]] 
    lista = pascal(x-1)  
    list = [1] 
    for i in range(1,x-1): 
        list.append(lista[x-2][i-1] + lista[x-2][i]) 
    list.append(1)
    lista.append(list) 
    return lista 

def main():
    T=True
    while T:
        Q = int(input('\nPara saber el resultado de la factorial de un numero presiona "1".\nPara saber los pasos de la serie fibonacci hasta un numero n presiona "2".\nPara multiplicar un numero por otro presione "3".\nPara imprimir un Triangulo de Pascal presione "4".\nPara saber el numero total de caminos que habra para llegar de una punta de una cuadricula a la otra punta presione "5"\nPara salir del programa presione "6":\n'))
        if Q == 1:
            x = int(input('\nIntrodusca el numero: '))
            print('\nEl resultado es',factorial(x))
        if Q == 2:
            x = int(input('\nIntrodusca el numero: '))
            print('\nEl resultado es',fibo(x))
        if Q == 3:
            x = int(input('\nIntrodusca el primer numero: '))
            y = int(input('\nIntrodusca el segundo numero: '))
            print('\nEl resultado es',multi(x,y-1))
        if Q == 4:
            x = int(input('\nIntrodusca el numero de pisos del triangulo: '))
            z = pascal(x)
            s = ' '
            for i in range(len(z)):
                print(z[i])
        if Q == 5:
            x = int(input('\nIntrodusca el primer numero de largo y ancho de la cuadricula: '))
            z =(pascal(x * 2-1))
            print('\nEl resultado es',z[x*2-2][x-1],'caminos')
        if Q == 6 or Q == '':
            T=False
    print('\n\n\nAdios')
if __name__ == "__main__":
    main()

