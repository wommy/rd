# ask user for location and title

location = input('location? ')
#print(location)
title = input('title? ')
#print(title)

# import datetime
import datetime

# format date - MM_DD_HHMM
date = ''
date += datetime.datetime.now().strftime('%m')
date += '_'
date += datetime.datetime.now().strftime('%d')
date += '_'
date += datetime.datetime.now().strftime('%H')
date += datetime.datetime.now().strftime('%M')
# print(filename)

# new file name w/ format: 'date-location-title'
filename = date+'-'+location+'-'+title

# create new file with filename
f= open(str(filename),"w+")

# write long date to file
f.write(str(datetime.datetime.now())+'-'+location+'-'+title)
f.close()

