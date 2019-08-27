import MySQLdb, csv
db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='ariag25',db = 'mydb')
c = db.cursor()
c.execute("SELECT * FROM testtable2 ORDER BY id DESC LIMIT 6")
for i in range (c.rowcount):
		
	row=c.fetchone()
	print row
c.close()
db.commit()
db.close()
