'''Escribir una función que reciba una lista de enteros.
En base a esta lista dibujar una serie de asteriscos.
Ejemplo de entrada: [3, 2, 5, 1, 6]
Salida: 
      '***'
      '**'
      '*****'
	  '*'
	  '******' '''

def Graphix():
    a = input("Ingresa una coleccion de numeros separados por comas ',' : ")
    b = a.split(",")
    c = list(map(int, b))

    for  i in range(0,len(c)):
        print(("*") * c[i])

def main():
	Graphix()

if __name__ == "__main__":
	main()