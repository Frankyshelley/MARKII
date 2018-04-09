import time
import sys
from sensor import sensor

import socket, pickle
from pid2 import pid
try:
	from motor import motor
except ImportError:
	print(ROJO +'FALLO CRITICO')
	print(BLANCO +'fallo módulo motor')
	sys.exit()
try:
	from MPU6050 import Gyro
except ImportError:
	print(ROJO+'FALLO CRITICO')
	print(BLANCO+'fallo importacion IMU')
try:
	from INA import ina
except ImportError:
	print(ROJO+ 'FALLO CRITICO')
	print(BLANCO+'fallo modulo bateria')





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
t =0
######################INICIO SENSORES##########################
bateria = ina()

time.sleep(1)
print('Nivel de Bateria: ',bateria.read(), 'V')
time.sleep(0.5)
print(VERDE + '[OK]' + BLANCO +'INA en marcha...')
giro = Gyro(1)
time.sleep(1)
print(VERDE + '[OK]'+ BLANCO + 'gyro en marcha...', giro.get_gyroffset())
time.sleep(1)
PID = pid()
print(VERDE + '[OK]' + BLANCO + 'PID iniciado......')

#####################MOTORES##################################

esc1 = motor('m1', 6, simulation=False)
esc2 = motor('m2', 13, simulation=False)
esc3 = motor('m3', 26, simulation=False)
esc4 = motor('m4', 19, simulation=False)

motores = [esc1, esc2, esc3, esc4]
for m in motores:
	m.start()
	time.sleep(1)
	m.setW(0)
	time.sleep(1)
	m.setW(10)
	time.sleep(1)
	m.setW(0)
		
print(VERDE + '[OK]' + BLANCO + 'motores armados')
##############################################################3

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, puerto))
server.listen(5)
print('Esperando Conexión..........')

try:
        
        for m in motores:
                m.setWLimits(10,100)
        init_t = time.time()
        tot= 0
        while True:
                t_prev = tot
                tot = time.time()-init_t
                t = tot-t_prev
                g = giro.get_rotation(t)
                b = bateria.read()
                x = g[0] 
                y = g[1] 
                z = g[2] 
                datos =[x,y,z,b]
                print(datos)
                time.sleep(1)


                                            
finally:

	for m in motores:
		m.stop()