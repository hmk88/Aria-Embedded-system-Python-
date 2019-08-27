import MySQLdb as mdb
import csv
# set credentilas
db_user = 'root'
db_pass = 'ariag25'
db_schema = 'mydb'

# set databases dictionary
dbs = '127.0.0.1'
    

# set sql query
db_query = "select * from data1 ORDER BY id DESC LIMIT 6;"

# for cycle to extract data from all databases
# wirte results in separated csv files
con = None
con = mdb.connect(dbs, db_user, db_pass, db_schema)
cur = con.cursor()
cur.execute(db_query)
for i in range (cur.rowcount):
    rows = cur.fetchone()
    out_file = csv.writer(open('out.csv', "wb"))
    columns = [i[1] for i in cur.description]
    out_file.writerow(columns)
    out_file.writerows(rows)
con.close()

