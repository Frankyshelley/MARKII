#!/usr/bin/python


import smbus, math, time

class Gyro:

	def __init__(self,rev):
		self.power_1 = 0x6b
		self.power_2 = 0x6c
		self.bus = smbus.SMBus(rev)
		self.address = 0x68
		self.bus.write_byte_data(self.address, self.power_1, 0)

	def read_byte(self,adr):
		return self.bus.read_byte_data(self.address, adr)

	def read_word(self,adr):
		high = self.read_byte(adr)
		low = self.read_byte(adr+1)
		val = (high << 8) + low
		return val

	def read_word_2c(self,adr):
		val = self.read_word(adr)
		if (val >= 0x8000):
			return -((65535 - val) + 1)
		else:
			return val

	def dist(self,a,b):
		return math.sqrt((a*a)+(b*b))

	def get_y_rotation(self,x,y,z):
		radians = math.atan2(x, self.dist(y,z))
		return -math.degrees(radians)

	def get_x_rotation(self,x,y,z):
		radians = math.atan2(y, self.dist(x,z))
		return math.degrees(radians)
	

	def get_gyro(self,mode):
		if mode == 0:
			return [self.read_word_2c(0x43),self.read_word_2c(0x45),self.read_word_2c(0x47)]
		elif mode == 1:
			return [self.read_word_2c(0x43)/131,self.read_word_2c(0x45)/131,self.read_word_2c(0x47)/131]

	def get_accel(self,mode):
		if mode == 0:
			return [self.read_word_2c(0x3b),self.read_word_2c(0x3d),self.read_word_2c(0x3f)]
		elif mode == 1:
			return [self.read_word_2c(0x3b)/16384.0,self.read_word_2c(0x3d)/16384.0,self.read_word_2c(0x3f)/16384.0]

	def get_rotation(self):
		accel_x, accel_y, accel_z = self.get_accel(1)
		gyro_x, gyro_y, gyro_z = self.get_gyro(1)
		x = int(self.get_x_rotation(accel_x, accel_y, accel_z))
		y = int(self.get_y_rotation(accel_x, accel_y, accel_z))
		z = int(gyro_z)
		return [x,y,z]
