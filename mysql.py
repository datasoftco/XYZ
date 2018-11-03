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

