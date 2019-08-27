import MySQLdb

db=MySQLdb.connect(host="127.0.0.1",port=3306,db="mydb",user="root",passwd="ariag25")

cur = db.cursor()
cur.execute("SELECT * FROM testtable1;")

sql = "INSERT INTO testtable1(Wind direction,Wind speed,Temperature,Humidity, \
       Pressure, Rain accumulator, Heating temperature, Heating voltage) \
       VALUES ('10D','0.2M','22.7C','45.8P','1014.8H','0.00M','22.3C','0.0NGcc')" 
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()


rows = cur.fetchall()

for row in rows:
	print row
