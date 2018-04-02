import time
import math
import mpu6050
class sensor:

	def __init__(self):
		self.mpu = mpu6050.MPU6050()
		self.mpu.dmpInitialize()
		self.mpu.setDMPEnabled(True)
    	self.packetSize = mpu.dmpGetFIFOPacketSize() 
    	self.ypr= {}

	def imu(self):
    # Get INT_STATUS byte
	    mpuIntStatus = self.mpu.getIntStatus()
	  
	    if mpuIntStatus >= 2: # check for DMP data ready interrupt (this should happen frequently) 
	        # get current FIFO count
	        fifoCount = self.mpu.getFIFOCount()
	        
	        # check for overflow (this should never happen unless our code is too inefficient)
	        if fifoCount == 1024:
	            # reset so we can continue cleanly
	            self.mpu.resetFIFO()
	            print('FIFO overflow!')
	            
	            
	        # wait for correct available data length, should be a VERY short wait
	        fifoCount = self.mpu.getFIFOCount()
	        while fifoCount < self.packetSize:
	            fifoCount = self.mpu.getFIFOCount()
	        
	        result = self.mpu.getFIFOBytes(self.packetSize)
	        q = self.mpu.dmpGetQuaternion(result)
	        g = self.mpu.dmpGetGravity(q)
	        ypr = self.mpu.dmpGetYawPitchRoll(q, g)
	        
	        z =round(self.ypr['yaw'] * 180 / math.pi),
	        y =round(self.ypr['pitch'] * 180 / math.pi),
	        x =round(self.ypr['roll'] * 180 / math.pi)
	    	return [x,y,z]
	        # track FIFO count here in case there is > 1 packet available
	        # (this lets us immediately read more without waiting for an interrupt)        
	        fifoCount -= self.packetSize  