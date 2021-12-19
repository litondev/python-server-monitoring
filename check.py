import psutil
import time
from datetime import datetime

# CPU
print("Total Cpu : "+str(psutil.cpu_count()))
print("Total All Cpu Usage % : "+str(psutil.cpu_percent(interval=1, percpu=True)))

# RAM
print(f"{round(psutil.virtual_memory().total / (2 ** 20)) / 1000} Gb Total")
print(f"{round(psutil.virtual_memory().available / (2 ** 20)) / 1000 } Gb Tersedia")
print(f"{round(psutil.virtual_memory().used / (2 ** 20)) / 1000 } Gb Digunakan")
print(f"{round(psutil.virtual_memory().free / (2 ** 20)) / 1000 } Gb Free")

# SWAP
print(f"{psutil.virtual_memory().percent} Percent")
print(f"{round(psutil.swap_memory().total / (2 ** 20 )) / 1000} Gb Total Swap")

# DISK
print(psutil.disk_usage("/"))

# BOOT TIME
print(datetime.fromtimestamp(psutil.boot_time()));

# DURASI SECOND
 # 31536000 => Tahun
 # 86400 => Day
 # 3600 => Hour
 # 60 => minute 
print(divmod(time.time() - psutil.boot_time(),3600)[0])

# GET ALL DURATION
days    = divmod(time.time() - psutil.boot_time(), 86400)        
hours   = divmod(days[1], 3600)               
minutes = divmod(hours[1], 60)               
seconds = divmod(minutes[1], 1)
print("Time between dates: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))

# USER LOGIN
print(psutil.users())

