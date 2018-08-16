import os
'''Hacer una clase alumno
-nombre
-promedio
-grupo

funcion recursiva de ordenamiento 
A) Promedio ordenado
B) Alfabetico alfabetico


Funcion de almacenamiento de alumnos en archivos 1 archivo por grupo

desde la terminal preguntar por el tipo de ordenamiento

poder agregar un almuno nuevo
donde preguntes nombre promedio y gurpo. '''

class alumno:
    def __init__(self,nombre,promedio,grupo):
        self.nombre = nombre
        self.promedio = promedio
        self.grupo = grupo

def grupos():
    #2016A
    a = []
    #2016B
    b = []
    #2017A
    c = []
    #2017B
    d = []
    #2018A
    e = []
    #2018B
    f = []
    with open('Estudiantes.txt','r') as Estudiantes:
        lines = Estudiantes.readlines()
    for i in range(len(lines)):
        lista = lines[i].split(',')
    
        if lista[2] == ' 2016A\n' :
            a.append(lines[i])
        if lista[2] == ' 2016B\n':
            b.append(lines[i])
        if lista[2] == ' 2017A\n':
            c.append(lines[i])
        if lista[2] == ' 2017B\n':
            d.append(lines[i])
        if lista[2] == ' 2018A\n':
            e.append(lines[i])
        if lista[2] == ' 2018B\n':
            f.append(lines[i])
    File1 = open('2016A.txt','w')
    for i in range(len(a)):
        File1.write(str(a[i]))
    File1.close
    File1 = open('2016B.txt','w')
    for i in range(len(b)):
        File1.write(str(b[i]))
    File1.close
    File1 = open('2017A.txt','w')
    for i in range(len(c)):
        File1.write(str(c[i]))
    File1.close
    File1 = open('2017B.txt','w')
    for i in range(len(d)):
        File1.write(str(d[i]))
    File1.close
    File1 = open('2018A.txt','w')
    for i in range(len(e)):
        File1.write(str(e[i]))
    File1.close
    File1 = open('2018B.txt','w')
    for i in range(len(f)):
        File1.write(str(f[i]))
    File1.close   

def addAlumno(Alumnos):
    x = str(input('¿cual es el nombre de la persona?: '))
    y = str(input('¿cual es su grupo?: '))
    z = str(input('¿cual es su Promedio?: '))
    estudiantes = open('Estudiantes.txt','a')
    estudiantes.write(str(x) +', '+ str(z)+', '+str(y)+str('\n'))
    a = len(Alumnos)+1 
    a = alumno(x,z,y)
    Alumnos.append(a)
    estudiantes.close
    return Alumnos

def main():
    ciclo = True
    Alumnos = []
    while ciclo:
        #Este with hace una lista  de el archivo estudiantes, donde cada objeto es una linea.
        with open('Estudiantes.txt','r') as Estudiantes:
            lines = Estudiantes.readlines()
        #Este for transforma cada linea del archivo en un objeto clase alumno.
        for i in range(len(lines)):
            lista = lines[i].split(', ')
            x = alumno(lista[0],float(lista[1]),lista[2])
            Alumnos.append(x)
        ciclo = False
    print(len(Alumnos))

    

    #addAlumno(Alumnos)
    
    
if __name__ == "__main__":
    main()