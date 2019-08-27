import MySQLdb

db=MySQLdb.connect(host="127.0.0.1",port=3306,db="mydb",user="root",passwd="ariag25")

cur = db.cursor()
cur.execute("SELECT * FROM dbt1;")

cur.execute('INSERT INTO dbt1 (Wind_direction, Wind_speed, Temperature, Humidity, Pressure, Rain_accumulator, 		Heating_temperature, Heating_voltage, Date, Time) VALUES (2,2,3,4,5,6,7,8,9,10)') 


# Execute the SQL command
try:
	# Execute the SQL command
	#cur.execute(sql)
	# Commit your changes in the database
   	db.commit()
	print "Successfully saved the data into database"
	time.sleep(2)

except:
	# Rollback in case there is any error
	db.rollback()
	print "Error in entering data"

db.close()
