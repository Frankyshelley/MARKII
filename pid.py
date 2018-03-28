

class pid(object):

        def __init__(self, P=2, I=0, D=1, Derivator=0, Integrator=0, Integrator_max=10, Integrator_min=-10):
                self.Kp=P
                self.Ki=I
                self.Kd=D
                self.Derivator=Derivator
                self.Integrator=Integrator
                self.Integrator_max=Integrator_max
                self.Integrator_min=Integrator_min
                self.set_point_pich=0
                self.error_pich=0
                self.set_point_roll=0
                self.error_roll=0
                self.set_point_yaw=0
                self.error_yaw=0
                

        def update_pich(self,current_value_pich):
                self.error_pich = self.set_point_pich - current_value_pich
                self.P_value = self.Kp * self.error_pich
                self.D_value = self.Kd * ( self.error_pich - self.Derivator)
                self.Derivator = self.error_pich
                self.Integrator = self.Integrator + self.error_pich

                if self.Integrator > self.Integrator_max:
                        self.Integrator = self.Integrator_max
                elif self.Integrator < self.Integrator_min:
                        self.Integrator = self.Integrator_min
                        
                self.I_value = self.Integrator * self.Ki
                PID = self.P_value + self.I_value + self.D_value
                correction_pich = round(PID)
                return correction_pich
        
        def setPoint_pich(self,set_point_pich):
                self.set_point_pich = set_point_pich
                self.Integrator=0
                self.Derivator=0

        def update_roll(self,current_value_roll):
                self.error_roll = self.set_point_roll - current_value_roll
                self.P_value = self.Kp * self.error_roll
                self.D_value = self.Kd * ( self.error_roll - self.Derivator)
                self.Derivator = self.error_roll
                self.Integrator = self.Integrator + self.error_roll

                if self.Integrator > self.Integrator_max:
                        self.Integrator = self.Integrator_max
                elif self.Integrator < self.Integrator_min:
                        self.Integrator = self.Integrator_min
                        
                self.I_value = self.Integrator * self.Ki
                PID = self.P_value + self.I_value + self.D_value
                correction_roll = round(PID)
                return correction_roll
        
        def setPoint_roll(self,set_point_roll):
                self.set_point_roll = set_point_roll
                self.Integrator=0
                self.Derivator=0

        def update_yaw(self,current_value_yaw):
                self.error_yaw = self.set_point_yaw - current_value_yaw
                self.P_value = self.Kp * self.error_yaw
                self.D_value = self.Kd * ( self.error_yaw - self.Derivator)
                self.Derivator = self.error_yaw
                self.Integrator = self.Integrator + self.error_yaw

                if self.Integrator > self.Integrator_max:
                        self.Integrator = self.Integrator_max
                elif self.Integrator < self.Integrator_min:
                        self.Integrator = self.Integrator_min
                        
                self.I_value = self.Integrator * self.Ki
                PID = self.P_value + self.I_value + self.D_value
                correction_yaw = round(PID)
                return correction_yaw
        
        def setPoint_yaw(self,set_point_yaw):
                self.set_point_yaw = set_point_yaw
                self.Integrator=0
                self.Derivator=0
        def setIntegrator(self, Integrator):
                self.Integrator = Integrator
        def setDerivator(self, Derivator):
                self.Derivator = Derivator
        def setKp(self,P):
                self.Kp=P
        def setKi(self,I):
                self.Ki=I
        def setKd(self,D):
                self.Kd=D
        def setmaxcorr(self,maxcorr):
                self.maxcorr= maxcorr
        def getIntegrator(self):
                return self.Integrator
        def getDerivator(self):
                return self.Derivator
