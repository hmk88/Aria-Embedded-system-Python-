
s=['>>0r0,Dm=109D,Sm=0.2M,Ta=22.7C,Ua=45.8P,Pa=1014.8H,Rc=0.00M,Th=22.3C,Vh=0.0NGcc']

a=[]
for x in range(0, 9):
	a.append([i.split(',',9)[x] for i in s])

print a
#wind direction
Dm=[i.split('=',1)[1] for i in a[1]]
#wind speed
Sm=[i.split('=',1)[1] for i in a[2]]
#air temperature
Ta=[i.split('=',1)[1] for i in a[3]]
#relative humidity
Ua=[i.split('=',1)[1] for i in a[4]]
#air pressure
Pa=[i.split('=',1)[1] for i in a[5]]
#rain accumulator
Rc=[i.split('=',1)[1] for i in a[6]]
#heating temperature
Th=[i.split('=',1)[1] for i in a[7]]
#heating voltage
Vh=[i.split('=',1)[1] for i in a[8]]

print Dm,Sm,Ta,Ua,Pa,Rc,Th,Vh

