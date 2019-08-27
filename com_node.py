#Author :  Hafiz Haq <Hafiz.haq@uwasa.fi>


########################Main Program###############################

import serial
import time
import ablib
import MySQLdb
import datetime
#Initializing and configuring port 


##################################

#Start
	
while 1:
	
		print "USB A ON"
		#Power_USB_A.on()
		#time.sleep(5)
		usb = serial.Serial()
		usb.port = "/dev/ttyUSB4"
		usb.baudrate = 115200
		usb.bytesize = serial.EIGHTBITS
		usb.parity = serial.PARITY_NONE
		usb.stopbits = serial.STOPBITS_ONE
		usb.timeout = 1
		#time.sleep(2)
		usb.open()
		time.sleep(2) 
		out = usb.read(5)
		#time.sleep(1)
		#print ">>" + out
		out1 = int(out.encode('hex'), 16)
		print ">>"
		print out1		
		#time.sleep(1)
		#s=out.split(',',8)
		usb.close()
		#time.sleep(1)
		
		#Connecting to the database
		db=MySQLdb.connect(host="127.0.0.1",port=3306,db="mydb",user="root",passwd="ariag25")
		cur = db.cursor()
		cur.execute("SELECT * FROM node;")
		
		cur.execute('INSERT INTO node (Temperature) VALUES ("%s")' %(out1)) 

		try:
			# Execute the SQL command
			#cur.execute(sql)
			# Commit your changes in the database
   			db.commit()
			print "Successfully saved the data into database"
			#time.sleep(2)
		except:
			# Rollback in case there is any error
			db.rollback()
			print "Error in entering data"

		db.close()
		#Power_USB_A.off()	
		#print "USB A Off"
		#print "Next reading after 10 minutes"
		#This is the time for the next cycle 
		time.sleep(1) 
			

#End
