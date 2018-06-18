def AreaT():
	a = input("Ingrese del triangulo la base y la altura separado por comas: ")
	a = a.split(",")
	a = list(map(int, a))	
	A = ((a[0]*a[1])/2)
	print(A)

def main():
	AreaT()
if __name__ == "__main__":
	main()
