from ina219 import INA219



class ina:
    def __init__(self):
        self.ina = INA219(shunt_ohms=0.1, max_expected_amps=1, address=0x40)
        self.ina.configure(voltage_range=self.ina.RANGE_16V,bus_adc=self.ina.ADC_128SAMP,shunt_adc=self.ina.ADC_128SAMP)
    def read(self):
        self.v = self.ina.voltage()
        return self.v
    
