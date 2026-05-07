class RecentCounter:

    def __init__(self):
        self.start=0
        self.end=0
        self.records=[0]*10000

    def ping(self, t: int) -> int:
        while (self.start<self.end and (t-self.records[self.start]>3000)):
            self.start+=1
            
        self.records[self.end]=t
        self.end+=1

        return self.end-self.start
