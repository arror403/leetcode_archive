class MyCalendarThree:

    def __init__(self):
        self.timeline=SortedDict()
        # self.timeline.setdefault(default=0)

    def book(self, startTime: int, endTime: int) -> int:
        if startTime not in self.timeline: self.timeline[startTime]=0
        self.timeline[startTime]+=1
        if endTime not in self.timeline: self.timeline[endTime]=0
        self.timeline[endTime]-=1
        
        ongoing=0
        k=0
        for v in self.timeline.values():
            ongoing+=v
            k=max(k, ongoing)

        return k