#Map: es una coleccion de datos organizados en pares(key:value) myDirectory={"uno": 1, "dos" : 2, "tres" :3 }

#Escribir un archivo que contenga, nombre y cumpleaños  nombre : cumpleaños

'''agregar nombres y cumpleaños al directorio
    ·En la consola dar la opcion de agregar.
    ·primero: pedir nombre
    ·segundo: pedir cumpleaños
    ·Guardar en el mapa
    ·guardar en el archivo
'''  
import os
def indiceBD(agenda):
    nombre = str(input("Introdusca en nombre de la persona de la que quieres saber el cumpleaños: "))          
    print('El cumpleaños de', nombre ,agenda[nombre]) 
    
    
def addBD(agenda):
    x = str(input('¿cual es el nombre de la persona?'))
    y = str(input('¿cual es su fecha de cumpleaños?'))
    cumpleaños = open('cumpleaños.txt','a')
    cumpleaños.write(str('\n') + str(x) + str(':')+' '+str(y) )
    agenda [x]=y
    cumpleaños.close
    return agenda
    
    
def main():
    v = True
    while v:
        cumpleaños = 0
        agenda =  dict()
        z = []
        if os.path.exists('cumpleaños.txt')==False:
            cumpleaños = open("cumpleaños.txt",'w')
            cumpleaños.write("Migue: 1 de Marzo \nYeipi: 1 de Abril \nOswaldo: 12 de Mayo \nJorge: 28 de Mayo \nMario: 1 Septiembre \nRodo: 27 de Diciembre")
            cumpleaños.close
        cumpleaños = open("cumpleaños.txt",'r+')
        directorio = cumpleaños.read()
        x = directorio.split('\n')
        for i in range(len(x)):
            z.append(x[i])
        for i in range(len(z)):
            f = z[i].split(':')
            agenda[f[0]] = f[1]
        cumpleaños.close
        v = False    
    x = True
    while (x) :
        x = int(input('\nIntrodusca 1 para saber el cumpeaños de una persona. \nSi no esta esa persona en la lista y desea agregarla introdusca 2.\nSi no desea hacer nada mas precione 3: '))
        if x == 1:
            indiceBD(agenda)
        if x == 2:
            addBD(agenda)
        if x == 3:
            x = False
    print('Adios')
if __name__ =="__main__":
    main()

    