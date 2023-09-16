import mysql.connector 

dataBase = mysql.connector.connect(
    host  = 'localhost',
    user = 'root',
    passwd = 'Thort_3270'
)

cursorobject = dataBase.cursor()

cursorobject.execute("CREATE DATABASE test")

print("ALL DONE")