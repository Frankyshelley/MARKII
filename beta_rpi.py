import socket,pickle
import time
import select
from INA import ina
from pymultiwii import MultiWii



#MSP = ROLL/PITCH/YAW/THTROTTLE/AUX1/AUX2/AUX3/AUX4
# mando = [self.trothle,self.yaw,self.pich,self.roll,self.b1,self.b2]

ROLL = 1500
PITCH = 1500
YAW = 1500
TROTHLE = 1000
Done = False
mando =[0,0,0,0,0,0]
print 'lanzando video.......'
subprocess.call('bash stream.sh', shell =True)
time.sleep(2)
print 'video lanzado'
ina= ina()
serialport = '/dev/ttyUSB0'
placa = MultiWii(serialport)
print 'conexion placa NAZE32 establecida', serialport
roll = 1500
pitch = 1500
yaw = 1500
trothle = 1000

UDP_IP = '0.0.0.0'
UDP_PORT = 10000
UDP_HOST = '192.168.1.36'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind( (UDP_IP,UDP_PORT) )
sock.setblocking(0)
bufer = 2048
print 'Socket udp creado con exito'
arm= 0

print 'Iniciando bucle principal'
while Done == False:
	
	bat = ina.read()
	if boton_up == 12 and arm == 0:
		placa.arm()
		arm = 1
	elif boton_up == 12 and arm ==1:
		placa.disarm()
		arm = 0
	if arm ==1:
		data =[roll,pitch,yaw,trothle,1000,1000,1000,1000]
		placa.sendCMDreceiveATT(16,MultiWii.SET_RAW_RC,data)
		x = int(placa.attitude['angx'])
		y = int(placa.attitude['angy'])
		z = int(placa.attitude['heading'])
		array = [x,y,z,bat]
		msg = pickle.dumps(array)
		sock.sendto(msg, (UDP_HOST,UDP_PORT))
	elif arm ==0:
		placa.getData(MultiWii.ATTITUDE)
		x = int(placa.attitude['angx'])
		y = int(placa.attitude['angy'])
		z = int(placa.attitude['heading'])
		array = [x,y,z,bat]
		msg = pickle.dumps(array)
		sock.sendto(msg, (UDP_HOST,UDP_PORT))
	HayDatosSocket = select.select([sock],[],[],0.5)
	if HayDatosSocket[0]:
		Socketdata = sock.recv(bufer)  
		mando = pickle.loads(Socketdata)
	roll = ROLL + mando[3]
	pitch = PITCH + mando[2]
	yaw = YAW + mando[1]
	trothle = TROTHLE + mando[0]
	boton_up = mando[5]
	boton_down = mando[4]


sock.close()








