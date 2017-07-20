#  04_05 Pretty time

from datetime import datetime

now = datetime.now()

print str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
