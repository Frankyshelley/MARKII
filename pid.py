from time import time,sleep


class pid(object):

    def __init__(self,kp=3,ki=0,kd=1,maxCorr=10):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previousTime = 0.0
        self.I = 0
        self.P =0
        self.D = 0
        self.previousError = 0.0
        self.init=True
        self.maxCorr=maxCorr


    def calc(self, error):
        if self.init:
            self.previousTime = time()
            self.init=False
            return 0
        else:
            currentTime = time()
            stepTime = currentTime - self.previousTime

            self.P = error * self.kp
            self.I += (error * stepTime) * self.ki
            self.D = (error - self.previousError) / stepTime * self.kd


            correction = self.P + self.I + self.D
            self.previousTime = currentTime
            self.previousError = error
            
            correction = round(correction)

            if correction>self.maxCorr:
                correction=self.maxCorr
            if correction<-self.maxCorr:
                correction=-self.maxCorr
            return correction
