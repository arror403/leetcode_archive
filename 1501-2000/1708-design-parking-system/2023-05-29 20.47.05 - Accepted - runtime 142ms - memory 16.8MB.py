class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.A = [big, medium, small]

    def addCar(self, carType):
        if carType not in [1, 2, 3]:
            raise ValueError("Invalid carType. Allowed values are 1, 2, or 3.")
        
        self.A[carType - 1] -= 1
        return self.A[carType - 1] >= 0
        
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)