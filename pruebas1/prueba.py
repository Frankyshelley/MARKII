 # Pruebas Rpi
ROJO = '\033[1;31m'
VERDE = '\033[1;32m'
BLANCO = '\033[0;0m'

print('''	(  ____ \(  ____ )(  ___  )( (    /|| \    /\|\     /|
	| (    \/| (    )|| (   ) ||  \  ( ||  \  / /( \   / )
	| (__    | (____)|| (___) ||   \ | ||  (_/ /  \ (_) / 
	|  __)   |     __)|  ___  || (\ \) ||   _ (    \   /  
	| (      | (\ (   | (   ) || | \   ||  ( \ \    ) (   
	| )      | ) \ \__| )   ( || )  \  ||  /  \ \   | |   
	|/       |/   \__/|/     \||/    )_)|_/    \/   \_/


		         .-""-"-""-.
		        /           
 			| .--.-.--. |
		        |` >       `|
		        | <         |
		        (__..---..__)
		       (`|\o_/ \_o/|`)
		        \(    >    )/
		      [>=|   ---   |=<]
		         \__\   /__/
		             '-'
###############################################################
###############################################################''')

import time
import sys

try:
	from motor import motor
except ImportError:
	print(ROJO +'FALLO CRITICO')
	print(BLANCO +'fallo módulo motor')
	sys.exit()
from sensor import sensor
#######################VARIABLES##############################
x = 0
y = 0
z = 0
datos = []
trothle = 0
pich = 0
roll = 0
yaw = 0
error_pich = 0
error_roll= 0
error_yaw = 0
final_pich = 0
final_roll = 0
final_yaw= 0
motor1 = 0
motor2 = 0
motor3 = 0
motor4 = 0
ip = "192.168.1.101"
puerto = 5000
######################INICIO SENSORES##########################
gyro = sensor()
time.sleep(2)
print(VERDE +'[OK]'+ BLANCO +'sensores Activos...')
#####################MOTORES##################################

esc1 = motor('m1', 6, simulation=False)
esc2 = motor('m2', 13, simulation=False)
esc3 = motor('m3', 26, simulation=False)
esc4 = motor('m4', 19, simulation=False)

motores = [esc1, esc2, esc3, esc4]
for m in motores:
	m.start()
	m.setW(0)
	
		
print(VERDE + '[OK]' + BLANCO + 'motores armados')
##############################################################3
a = input('al cielo:')
b = gyro.imu()
z_prev = b[2]
for m in motores:
        m.setW(10)
while True:
        giro  = gyro.imu()
        z = giro[2] - z_prev
        z_prev = z
        x = giro[0]
        y = giro[1]

        print(x,y,z)


   
for m in motores:
        m.stop()
