'''Crear una función la cual reciba un texto como si fuera el nombre de un archivo.
 La función deberá imprimir en la pantalla un mensaje con la extensión del archivo.
 Ejemplo de entrada: hello.exe.
 Salida: La extensión es: exe.'''

def llave(i):
	print((i.split(".")[1]) + str(": es la extencion de tu archivo" ))

def main():
	x = str(input("Introducir archivo: "))
	llave(x)

if __name__ == "__main__":
	main()