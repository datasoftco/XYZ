import mysql.connector

mydb = mysql.connector.connect(
  host="www.xyz.org",
  user="administrator",
  passwd="githubGnu@2020",
  database="xyzDB"
)

print(xyzDB)
 mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for r in mycursor:
  print(r)
