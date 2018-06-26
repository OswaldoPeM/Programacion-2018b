
import os

def directorio():
    print(os.getcwd())
    w = os.listdir(input("Ingresar una direccion para saber que hay dentro: "))
    
    for i in w:
        print(i)
    
def Saludos():
	archivo = open('Saludos.txt','w')
	archivo.write('Hola, mi nombre es Oswaldo Perez Macias:\nTe saludo desde mi primer archivo de texto.\n\nSaludos!')
	archivo.close()

def rutaAbsoluta():
     print(os.path.abspath(input("Ingresar una direccion y nombre de archivo para saber la direccion absoluta: ")))

def coincidencia():
    felices = open("felices.txt",'r')
    primos = open("primos.txt",'r')
    iguales = open('iguales.txt','w')
    x = felices.readlines()
    y = primos.readlines()
    for line in x:
        for line2 in y:
            if line == line2:
                iguales.write(line)
        

    iguales.close
    felices.close
    primos.close
    
def main():
    int(input("Para saber el archivos y directorio introdusca 1.\nPara crear un archivo hermoso introdusca 2.\nPara saber ruta absoluta de un archivo introdusca 3.\nPara crear un archivo de texto con las coincidencias de las listas que nos dejo de tarea presione 4.(concidere tener los archivos .txt en la carpeta.):\n"))
    if (z == 1):
        directorio()
    if (z == 2):
        Saludos()
    if (z == 3):
        rutaAbsoluta()
    if (z == 4):
        coincidencia()
if __name__ == "__main__":
	main()