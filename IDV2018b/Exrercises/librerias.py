import calendar

def Showcalendar(year,month):
    
    print(calendar.month(year,month))

def PrintNumbers(num):
    for i in range(num):
        print(i)

def main():
    year = int(input("Escribe el año: "))
    month = int(input("Escribe el mes: "))
    Showcalendar(year,month) 

    PrintNumbers(month)
   
if __name__ == "__main__":
    main()