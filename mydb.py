#install mysql
#pip install mysql, mysql-connector, mysql-connector-python

import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'MySql@3306'
)

cursorobject = db.cursor()

cursorobject.execute("CREATE DATABASE appdata")

print("All Done!...")
