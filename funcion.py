'''funcion: un bloque de codigo el cual tiene un propocito especifico. esta puede tener parametros de entrada(inputs) y valores de retorno(output) [resultado]. se puede ejecutar (llamar) desde otras partes del programa'''
#funcion de saludo
def Saludar():
	print("hola mundo desde mi funcion!")
#funcion de suma
def Suma(numX,numY):
	if(type(numX)) != int or (type(numY)) != int:
		print("Estas usando un tipo de dato incorrecto")
		return
	result = numX + numY
	return result
#funcion de multiplicacion
def multiplicacion(numX,numY):
	if(type(numX)) != int or (type(numY)) != int:
		print("Estas usando un tipo de dato incorrecto")
		return
	result = numX * numY
	return result
#funcion divicion 
def div(numX,numY):
	if(type(numX)) != int or (type(numY)) != int or (type(numY)) == 0 :
		print("Estas usando un tipo de dato incorrecto")
		return
	if (numY==0):
		print("chistosito")
		return
	result = numX / numY
	return result
#funcion del cuadraro
def cuadrado(numX):
	if(type(numX)) != int:
		print("Estas usando un tipo de dato incorrecto")
		return
	result = numX ** 2
	return result

def main():
	Saludar()
	print("Para sumar presiona '1' para multiplicar presiona '2' para dividir presiona '3' para elevar al cuadraro presiona '4' :")
	x = int(input())
	if x == 1:
		num1 = int(input("Escribe un numero: "))
		num2 = int(input("Escribe otro numero: "))
		result = Suma(num1,num2)
	if x == 2:
		num1 = int(input("Escribe un numero: "))
		num2 = int(input("Escribe otro numero: "))
		result = multiplicacion(num1,num2)
	if x == 3:
		num1 = int(input("Escribe un numero: "))
		num2 = int(input("Escribe otro numero: "))
		result = div(num1,num2)
	if x == 4:
		num1 = int(input("Escribe un numero: "))
		result = cuadrado(num1)


	print("El resultado es " + str(result))

if __name__ == "__main__":
	main()