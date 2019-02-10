import pyodbc
import csv

#Connection to SQL database
mycon=pyodbc.connect(driver='{SQL Server}', server='DBD01\DEV,51433', database='EDLETTERS', trusted_connection='yes')


mydict={}
cr = mycon.cursor()
#Extracting data from database
cr.execute('select AccIdn,UserID,DDate from dbo.LetterInfo')

record = cr.fetchall()

#Asking user to provide the date after which records should be processed i.e DDate >=ipdate
ipdate=input('Enter the dates for which you want to execute in YYYMMDD format')

#Creating dictionary 
for row in record :

    if (row[2])>= ipdate:
        print(row)
        ky=row[0]
        vl=row[1]
        mydict[ky] = vl

print(mydict.keys())
print(mydict.values())


//Writing data extracted in dictionary in csv file
csv_file = "C:\\Temp\\Letter_Info.csv"
try:

    w = csv.writer(open(csv_file, "w"))
    for key, val in mydict.items():
        w.writerow([key, val])
except IOError:
    print("I/O error")

