from datetime import timedelta, datetime
simdi = datetime.now()
result = datetime.now()
#result = simdi.day
#result = simdi.month
#result = simdi.year 

#result = datetime.ctime(simdi)
#result = datetime.strftime(simdi,"%Y %B %X %d %A")


t = '15 April 2021 hour 10:30:35'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

birhtday = datetime(2002,1,26,4,0,10)
result = datetime.timestamp(birhtday)  # saniyeye çevirir
result = datetime.fromtimestamp(result)  # normale çevirir.

result =  simdi - birhtday  # time delta 
print(simdi)
result = simdi + timedelta(days = 10) 



print(result)

