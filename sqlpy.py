import MySQLdb

db=MySQLdb.connect(host="127.0.0.1",port=3306,db="mydb",user="root",passwd="ariag25")

cur = db.cursor()

cur.execute("SELECT * FROM data1;")

sql = """INSERT INTO data1(Wind_direction,Wind_speed,Temperature,Humidity,Pressure,Rain_accumulator,Heating_temperature,Heating_voltage) VALUES ('2210D','0.2M','23.7C','45.8P','1014.8H','0.00M','22.3C','0.0NGcc');"""
try:
   # Execute the SQL command
   cur.execute(sql)
   # Commit your changes in the database
   db.commit()
   print "Successful"
except:
   # Rollback in case there is any error
   db.rollback()
   print "Error in entering data"

db.close()
