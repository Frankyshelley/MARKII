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
	from MPU6050 import Gyro
except ImportError:
	print(ROJO +'FALLO CRITICO')
	print(BLANCO +'Fallo en MPU')
	sys.exit()
import socket, pickle
from pid2 import pid
try:
	from motor import motor
except ImportError:
	print(ROJO +'FALLO CRITICO')
	print(BLANCO +'fallo módulo motor')
	sys.exit()
try:
	from INA import ina
except ImportError:
	print(ROJO +'FALLO CRITICO')
	print(BLANCO +'fallo módulo lectura de bateria')
	sys.exit()
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
bateria = ina()
b = bateria.read()
time.sleep(1)
print('Nivel de Bateria:', b , 'V')
time.sleep(0.5)
print(VERDE + '[OK]' + BLANCO +'INA en marcha...')
gyro= Gyro(1)
time.sleep(1)
print(VERDE + '[OK]'+ BLANCO + 'gyro en marcha...', gyro.get_rotation())
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
	print(m, 'armado')
	
print(VERDE + '[OK]' + BLANCO + 'motores armados')
##############################################################3

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, puerto))
server.listen(5)
print('Esperando Conexión..........')

try:
        while True:
                cliente, direccion = server.accept()
                print("Cliente conectado desde: ", direccion)
                motor.setWLimits(10,100)
                while True:
                        g = gyro.get_rotation()
                        b = bateria.read()
                        x = g[0] * -1
                        y = g[1] * -1
                        z = g[2] * -1
                        
                        if y <= 4: # quitar este if si cambias el MPU
                        	y = 0
                        if z <= 2:
                        	z = 0 
                        datos =[x,y,z,b]

                        timon = cliente.recv(4096)
                        array = pickle.loads(timon)
                        envio = pickle.dumps(datos)
                        cliente.send(envio)

                        
                        trothle = array[0]
                        if trothle < 0:
                        	trothle = 0

                        pich = array[2]
                        roll= array[3]
                        yaw = array[1]

                        
                        final_pich = PID.calc_pitch(y,pich)
                        
                        final_roll = PID.calc_roll(x,roll)
                     
                        final_yaw = PID.calc_yaw(z,yaw)
                        
                        motor1 = trothle - final_pich - final_roll + final_yaw
                        motor2 = trothle - final_pich + final_roll - final_yaw
                        motor3 = trothle + final_pich - final_roll - final_yaw
                        motor4 = trothle + final_pich + final_roll + final_yaw
                        esc1.setW(motor1)
                        esc2.setW(motor2)
                        esc3.setW(motor3)
                        esc4.setW(motor4)
finally:

	for m in motores:
		m.stop()
