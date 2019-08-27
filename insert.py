import MySQLdb

db=MySQLdb.connect(host="127.0.0.1",port=3306,db="mydb",user="root",passwd="ariag25")

cur = db.cursor()
cur.execute("SELECT * FROM data;")

sql = """INSERT INTO weather(Wind_direction,Wind_speed,Temperature,Humidity, \
       Pressure, Rain_accumulator, Heating_temperature, Heating_voltage) \
       VALUES ('10D','0.2M','22.7C','45.8P','1014.8H','0.00M','22.3C','0.0NGcc');""" 

   # Execute the SQL command
cur.execute(sql)
   # Commit your changes in the database
db.commit()

rows = cur.fetchall()

for row in rows:
	print row

# disconnect from server
db.close()
