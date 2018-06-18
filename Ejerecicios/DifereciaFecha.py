from datetime import date
def DifDate(x,y):
	print ((y-x).days)

def main():
	a = input("Ingrese primera fecha DD,MM,YYYY: ")
	a = a.split(",")
	a = list(map(int, a))
	b = input("Ingrese segunda fecha DD,MM,YYYY: ")
	b = b.split(",")
	b = list(map(int, b))

	x = date(a[2],a[1],a[0])
	y = date(b[2],b[1],b[0])
	
	DifDate(x,y)

if __name__ == "__main__":
	main()