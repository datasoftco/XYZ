import mysql.connector

mydb = mysql.connector.connect(
  host="www.xyz.org",
  user="administrator",
  passwd="githubGnu@2020",
  database="xyzDB"
)
print(xyzDB)


cursor = xyzDB.cursor()
cursor.execute("CREATE DATABASE ListOfCodesDB")


cursor = xyzDB.cursor()
cursor.execute("SHOW DATABASES")

for r in cursor:
  print(r)

  
cursor.execute("CREATE TABLE Subscribers (name VARCHAR(255), Description VARCHAR(255))")

cursor.execute("CREATE TABLE Coders (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#INSERT

sql = "INSERT INTO Coders (name, address) VALUES (%s, %s)"
val = ("Abdulmajeed", "Ca 1005")
cursor.execute(sql, val)
xyzDB.commit()

print(cursor.rowcount, "record inserted.")


#------------------------------------------------
#Insert Multiple Rows
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


#Get Inserted ID
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

#------------------------------------------------
#Select From a Table

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
