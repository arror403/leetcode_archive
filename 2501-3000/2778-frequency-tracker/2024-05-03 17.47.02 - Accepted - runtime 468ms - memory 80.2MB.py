class FrequencyTracker:

    ##### improved by chatGPT #####

    def __init__(self):
        self.d = defaultdict(int)
        self.f = defaultdict(set)

    def add(self, number: int) -> None:
        q = self.d[number] = self.d[number]+1
        self.f[q].add(number)
        self.f[q-1].discard(number)

    def deleteOne(self, number: int) -> None:
        if self.d[number]:
            q = self.d[number] = self.d[number]-1
            self.f[q].add(number)
            self.f[q+1].discard(number)

    def hasFrequency(self, frequency: int) -> bool:
        return True if self.f[frequency] else False