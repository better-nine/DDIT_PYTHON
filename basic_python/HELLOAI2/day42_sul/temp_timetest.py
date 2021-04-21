import time
t = time.time()
print(t)

import datetime 
now = datetime.datetime.now()
formattedDate = now.strftime("%Y%m%d_%H%M%S")
print(now)
print(formattedDate)