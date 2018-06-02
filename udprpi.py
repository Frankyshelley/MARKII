class comunicacion(threading.Thread):
        def __init__(self, UDP_IP='192.168.1.101',UDP_HOST='192.168.1.36',UDP_PORT=10000):
                threading.Thread.__init__(self)
                self.UDP_IP = UDP_IP
                self.UDP_HOST = UDP_HOST
                self.UDP_PORT = UDP_PORT
                self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                self.sock.bind( (self.UDP_IP,self.UDP_PORT) )
                self.sock.setblocking(0)
                self.buffer = 2048
                self.a =[]
                self.done = False
                print 'Socket UDP creado con exito'

                

                
        def run(self):
        	print 'Iniciando bucle........'
        	while self.done== False:
                        HayDatosSocket = select.select([self.sock],[],[],0.5)
                        if HayDatosSocket[0]:
                            Socketdata = sock.recv( self.buffer )  
                            self.a = pickle.loads(Socketdata)
        		# mando = [self.trothle,self.yaw,self.pich,self.roll,self.b1,self.b2]
		        
		        time.sleep(0.1)
                        msg = pickle.dumps(self.mando)
                        self.sock.sendto(msg, (self.UDP_HOST, self.UDP_PORT))
		              
		      
			
            
        def telemetria(self):
        	return self.
        def mando(self):
        	return self.a

        def stop(self):
        	print 'Parando hilo....'
        	self.done == True
        	print 'cerrando Socket......'
        	self.sock.close()
