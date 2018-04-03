import time
import math
import mpu6050
from ina219 import INA219
class sensor:

        def __init__(self):
                self.mpu = mpu6050.MPU6050()
                self.mpu.dmpInitialize()
                self.mpu.setDMPEnabled(True)
                self.packetSize = self.mpu.dmpGetFIFOPacketSize() 
                self.ypr= {}
                self.ina = INA219(shunt_ohms=0.1, max_expected_amps=1, address=0x40)
                self.ina.configure(voltage_range=self.ina.RANGE_16V,bus_adc=self.ina.ADC_128SAMP,shunt_adc=self.ina.ADC_128SAMP)

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
                    #print('FIFO overflow!')
                    
                    
                # wait for correct available data length, should be a VERY short wait
                fifoCount = self.mpu.getFIFOCount()
                while fifoCount < self.packetSize:
                    fifoCount = self.mpu.getFIFOCount()
                
                result = self.mpu.getFIFOBytes(self.packetSize)
                q = self.mpu.dmpGetQuaternion(result)
                g = self.mpu.dmpGetGravity(q)
                self.ypr = self.mpu.dmpGetYawPitchRoll(q, g)
                
                z =round(self.ypr['yaw'] * 180 / math.pi),
                y =round(self.ypr['pitch'] * 180 / math.pi),
                x =round(self.ypr['roll'] * 180 / math.pi)
                return [x,y,z]
                # track FIFO count here in case there is > 1 packet available
                # (this lets us immediately read more without waiting for an interrupt)        
                fifoCount -= self.packetSize
        def ina(self):
            self.v = self.ina.voltage()
            return self.v


