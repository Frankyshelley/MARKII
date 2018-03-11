
from motor import motor

motor1 = motor('m1', 6, simulation=False)
motor2 = motor('m1', 13, simulation=False)
motor3 = motor('m1', 26, simulation=False)
motor4 = motor('m1', 19, simulation=False)

motors = [motor1, motor2, motor3, motor4]

print('desconecta bateria')
print('pulsa intro')
res = raw_input()
try:
        for mitour in motors:
                mitour.start()
                mitour.setW(100)

	print('conecta bateria ')
	print('espera el beep-beep')

        res = raw_input()
	for mitour in motors:
                mitour.start()
                mitour.setW(0)
	print('espera los 3 beep de la bateria')
	print('beep largo de calibracion correcta')
	print('pulsa intro')
	res = raw_input()
	
	for mitour in motors:
                mitour.start()
                mitour.setW(10)
	res = raw_input()
finally:
  
        for mitour in motors:
                mitour.stop()

        print ("listo!")
        exit()
