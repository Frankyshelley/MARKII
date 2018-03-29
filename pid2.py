from time import time,sleep


class pid(object):

    def __init__(self,kp=3,ki=0,kd=1,maxCorr=10, minCorr=-10, I_min = -10, I_max= 10):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.I = 0
        self.P =0
        self.D = 0
        self.error_pitch=0
        self.error_roll = 0
        self.error_yaw = 0
        self.maxCorr= maxCorr
        self.minCorr = minCorr
        self.I_max= I_max
        self.I_min = I_min
        self.prev_error_pitch = 0
        self.prev_error_roll = 0
        self.prev_error_yaw = 0


    def calc_pitch(self, y, pitch):
        self.error_pitch = pitch - y
        self.P = self.kp * self.error_pitch
        self.I += self.ki * self.error_pitch
        if self.I > self.I_max:
            self.I = self.I_max
        elif self.I < self.I_min:
            self.I = self.I_min
        self.D = self.kd *(self.error_pitch - self.prev_error_pitch)
        correction = round(self.P + self.I + self.D)
        self.prev_error_pitch = self.error_pitch
        if correction > self.maxCorr:
            correction = self.maxCorr
        elif correction < self.minCorr:
            correction = self.minCorr
        return correction  

    def calc_roll(self, x, roll):
        self.error_roll = roll - x
        self.P = self.kp * self.error_roll
        self.I += self.ki * self.error_roll
        if self.I > self.I_max:
            self.I = self.I_max
        elif self.I < self.I_min:
            self.I = self.I_min
        self.D = self.kd *(self.error_roll - self.prev_error_roll)
        correction = round(self.P + self.I + self.D)
        self.prev_error_roll = self.error_roll
        if correction > self.maxCorr:
            correction = self.maxCorr
        elif correction < self.minCorr:
            correction = self.minCorr
        return correction       

    def calc_yaw(self, z, yaw):
        self.error_yaw = yaw - z
        self.P = self.kp * self.error_yaw
        self.I += self.ki * self.error_yaw
        if self.I > self.I_max:
            self.I = self.I_max
        elif self.I < self.I_min:
            self.I = self.I_min
        self.D = self.kd *(self.error_yaw - self.prev_error_yaw)
        correction = round(self.P + self.I + self.D)
        self.prev_error_yaw = self.error_yaw
        if correction > self.maxCorr:
            correction = self.maxCorr
        elif correction < self.minCorr:
            correction = self.minCorr
        return correction
    def pid_agresivo(self):
    	self.maxCorr = 30
    	self.minCorr = -30
    def pid_normal(self):
    	self.maxCorr= 10
    	self.minCorr = -10
    def setk(self,kp,ki,kd):
    	self.kp = kp
    	self.ki = ki
    	self.kd = kd
    def error(self, x,y,roll,pitch):
    	error_p = pitch -y
    	error_r = roll -x
    	return [error_p,error_r]
    	




