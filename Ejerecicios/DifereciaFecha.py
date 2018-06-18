'''Escribir una función que te diga los días que hay entre 2 fechas.
  La función deberá imprimir en la pantalla la cantidad de días que hay entre ambas fechas.
  Ejemplo de entrada: (15, 06, 2018) (19, 06, 2018)
  Salida: 4.
  *Usar la librería datetime. '''

def DifDate():
    from datetime import date
    a = input("Ingrese primera fecha DD,MM,YYYY: ")
    b = input("Ingrese segunda fecha DD,MM,YYYY: ")
    a = a.split(",")
    a = list(map(int, a))
    x = date(a[2],a[1],a[0])
    b = b.split(",")
    b = list(map(int, b))
    y = date(b[2],b[1],b[0])
    
    print ((y-x).days)

def main():
	DifDate()

if __name__ == "__main__":
	main()