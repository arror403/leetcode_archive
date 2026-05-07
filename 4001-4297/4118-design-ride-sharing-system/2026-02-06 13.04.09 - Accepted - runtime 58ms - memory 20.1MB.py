class RideSharingSystem:

    def __init__(self):
        self.r=deque()
        self.d=deque()

    def addRider(self, riderId: int) -> None:
        self.r.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.d.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.r and self.d:
            return [self.d.popleft(), self.r.popleft()]
        else:
            return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.r:
            self.r.remove(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)