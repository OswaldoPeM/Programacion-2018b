x = int(input("Ingresar pasos que va a dar en el ciclo fibbonacci que sea mayor a 5 y menor a 15: "))
print ()
x = x - 2
if (x > 13):
	x = 13
if (x < 3):
	x = 3
a = 1
b = 0	
print(b)
print(a)
for i in range (x):
	a= a + b
	b= a - b
	print (a)