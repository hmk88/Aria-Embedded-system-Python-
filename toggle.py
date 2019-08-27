import time
import ablib
 
Power_USB_A = ablib.Pin('N','7','high')
Power_USB_B = ablib.Pin('N','8','high')
Power_USB_C = ablib.Pin('N','9','high')

while True:

	Power_USB_B.off()

	Power_USB_C.off()

	print "USB A ON"
	Power_USB_A.on()
	
	time.sleep(15) 
	
	
