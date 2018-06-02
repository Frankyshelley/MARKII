
#! bin/python3

# subprocess.check_output("sudo iwlist wlan0 scan | egrep -i 'ESSID|quality|Frequency'", shell=True)
import datetime
import psutil
import shlex,subprocess
from datetime import timedelta
class rpi_status:

    def get_cpuload():
        cpuload = psutil.cpu_percent(interval=1, percpu=False)
        return str(cpuload)

    def get_cpu_temp():
        tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
        cpu_temp = tempFile.read()
        tempFile.close()
        return float(cpu_temp)/1000
    def wifi_name(): 
        wifi_name = subprocess.check_output("sudo iwlist wlan0 scan | egrep -i 'quality'", shell=True)
        return(wifi_name)
        
print(rpi_status.get_cpuload())
print(rpi_status.get_cpu_temp())
print(rpi_status.wifi_name())

