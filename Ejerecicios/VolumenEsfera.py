'''Escribir una función que calcule el volumen de una esfera.
La función deberá recibir el valor del radio.'''

def volumen():
    r = float(input("Introducir radio de la esfera en centimetros: "))
    v = (4/3) * 3.1416 * ((r)**3) 
    print("El volumen de tu esfera es de " + str(v) + str("centimetros"))

def main():
	
	volumen()

if __name__ == "__main__":
	main()