#Map: es una coleccion de datos organizados en pares(key:value) myDirectory={"uno": 1, "dos" : 2, "tres" :3 }

#Escribir un archivo que contenga, nombre y cumpleaños  nombre : cumpleaños
import os
def indiceBD():
    nombre = str(input("Introdusca en nombre de la persona de la que quieres saber el cumpleaños: "))
    cumpleaños = 0
    agenda =  dict()
    z = []
    if os.path.exists('cumpleaños.txt')==False:
        cumpleaños = open("cumpleaños.txt",'w')
        cumpleaños.write("Migue: 1 de Marzo \nYeipi: 1 de Abril \nOswaldo: 12 de Mayo \nJorge: 28 de Mayo \nMario: 1 Septiembre \nRodo: 27 de diciembre")
    elif os.path.exists('cumpleaños.txt'):
        cumpleaños = open("cumpleaños.txt",'r+')
    directorio = cumpleaños.read()
    x = directorio.split('\n')
    for i in range(len(x)):
        z.append(x[i])
    for i in range(len(z)):
        f = z[i].split(':')
        agenda[f[0]] = f[1]
            
    print('El cumpleaños de', nombre ,agenda[nombre]) 
    cumpleaños.close()

def main():
    indiceBD()
if __name__ =="__main__":
    main()

    