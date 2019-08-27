

import MySQLdb, csv
db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='ariag25',db = 'mydb')
c = db.cursor()
csv_data = csv.reader(file('out.txt'))
for row in csv_data:
  print row
  
  c.execute('INSERT INTO testtable2 (id, Wind_direction, Wind_speed,Temperature, Humidity, Pressure, Rain_accumulator, Heating_temperature,Heating_voltage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', row)
c.close()
db.commit()
db.close()
