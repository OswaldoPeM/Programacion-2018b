def Graphix():
    a = input("Ingresa una coleccion de numeros separados por comas ',' para expresar esos numero graficamente con asteriscos : ")
    b = a.split(",")
    c = list(map(int, b))

    for  i in range(0,len(c)):
        print(("*") * c[i])
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
def llave():
    i = str(input("Introducir archivo: "))
    print("\n" + str(i.split(".")[1]) + str(": es la extencion de tu archivo \n" ))
def AreaT():
	a = input("Ingrese del triangulo la base y la altura separado por comas: ")
	a = a.split(",")
	a = list(map(int, a))	
	A = ((a[0]*a[1])/2)
	print(A)
def volumen():
    r = float(input("Introducir radio de la esfera en centimetros: "))
    v = (4/3) * 3.1416 * ((r)**3) 
    print("El volumen de tu esfera es de " + str(v) + str("centimetros"))

def main():
	x = int(input("Introducir 1 para inerpretar numero graficamente mediante asteriscos. \nIntroducir 2 para saber cuantos dias hay entre dos fechas. \nIntroducir 3 para saber la extencion de un archivo. \nIntroducir 4 para saber el area de un triangulo. \nIntroducir 5 para saber el volumen de una esfera."))
	if (x==1):
		Graphix()
	if (x==2):
		DifDate()
	if (x==3):
		llave()
	if(x==4):
		AreaT()
	if(x==5):
		volumen()
	else:
		break

if __name__ == "__main__":
	main()

import sys
print(sys.version)