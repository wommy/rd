# ask user for topic
topic = input('topic?: ')

# import datetime
import datetime

# new time
time = datetime.datetime.now()

# for week in quarter
wm = str( int( int( time.strftime( "%W" ) ) % 13 + 1 ) )

# format for filename - YYq#-MMw#
filenameTime = time.strftime('%mw')+wm

# new file name w/ format: filenameTime-title.md
filename = filenameTime+'-'+topic+'.md'

# create new file with filename
f= open(filename,"w+")

# write frontmatter to file
f.write('''---
topic: '''+topic+'''
time: '''+time.strftime('%m-%d %H%M')+'''
place:
rambles:
---

''')
f.close()

