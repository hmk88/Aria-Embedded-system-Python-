import MySQLdb

count = 0
db=MySQLdb.connect(host="127.0.0.1",port=3306,db="mydb",user="root",passwd="ariag25")
cur = db.cursor()
count = cur.execute("SELECT * FROM dbt1;")
print count

while count >= 144:
	print "Success"
	cur.execute("DELETE FROM dbt1 LIMIT 1;")
	count = cur.execute("SELECT * FROM dbt1;")
	db.commit()

db.close()


