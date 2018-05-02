import socket
from threading import Thread
import sys
import pickle




class servidor():
	def __init__(self,host="192.168.1.101", port=5000)
	self.host = host
	self.port = port
	self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	self.sock.bind(str(self.host),int(self.port))
	self.sock.listen(1)

	self.array = [0,0,0,0,] #CAMBIAR SI SE AÑADE CAMPOS!!!!!
	self.respuesta= []
	self.conn = ''
	self.conexion = False

def aceptar_com(self):
	while True:
		try:
			self.conn, addr = self.sock.accept()
			self.conexion = True
		except:
			pass


def envio(self):
	try:
		while True:
			
			if self.conexion == True:
				mensaje = pickle.dump(self.array)
				self.conn.send(mensaje)
	except SocketError:
		pass



def recepcion(self):
	try:
		while True:
			if self.conexion == True:
				dato_respuesta = self.conn.recv(4096)
				self.respuesta = pickle.loads(dato_respuesta)
	except SocketError:
		pass


def start(self):
	print('Iniciando comunicaciones')
	aceptar_com= Thread(target=self.aceptar_com)
	aceptar_com.start()
	print('Iniciando hilo de envío')
	envio = Thread(target=self.envio)
	envio.start()
	print('Hilo de envío iniciado')
	print('Iniciando hilo de recepción')
	recepcion = Thread(target=self.recepcion)
	recepcion.start()
	print('Hilo recepcion iniciado')


def datos_mando(self):
	return self.respuesta
def envio_tm(self, array):
	self.array = array


def stop(self):
	aceptar_com.stop()
	envio.stop()
	recepcion.stop()
	self.sock.close()





