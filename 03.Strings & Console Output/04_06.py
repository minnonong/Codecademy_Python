#  04_06 Grand Finale

from datetime import datetime

now = datetime.now()

print str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
