def cuadricula():
    c= int(input('introduce un numero para generar un tablero cuadrado con esas dimensiones: ')) 
    a = '__'
    b = '|__'
    print((a.rjust(3))*c)
    for i in range(c):
         print('|__'+((b.rjust(1))*(c-1))+'|')
def main():
    cuadricula()
if __name__ == "__main__":
    main()