class Car:
    def __init__(self, init_mpg):
        self._mpg = init_mpg
        self.fuel_level = 0

    def addGas(self, fuel):
        self.fuel_level += fuel
    
    def drive(self, miles):
        self.fuel_level -= miles // self._mpg 
    
    def getGasLevel(self):
        return self.fuel_level