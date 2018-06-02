def Potencia(num1,num2 = 1):
	for x in range (num2):
		num1 *= num1
	return num1

def main():
	numero = int(input("Escribe un nunmero: "))

	print ("El numero al cuadrado es: " + str(Potencia(numero)))

if __name__ == "__main__":
	main()
