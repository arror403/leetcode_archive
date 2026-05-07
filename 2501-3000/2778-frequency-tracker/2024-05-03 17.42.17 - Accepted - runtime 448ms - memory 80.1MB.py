class FrequencyTracker:

    ##### improved by chatGPT #####

    def __init__(self):
        self.counter = {}
        self.frequency = {}


    def add(self, number: int) -> None:
        self.counter[number] = self.counter.get(number, 0) + 1
        freq = self.counter[number]
        if freq not in self.frequency:
            self.frequency[freq] = set()
        self.frequency[freq].add(number)
        if freq > 1:
            self.frequency[freq - 1].discard(number)


    def deleteOne(self, number: int) -> None:
        if number in self.counter and self.counter[number] > 0:
            freq = self.counter[number]
            self.counter[number] -= 1
            if self.counter[number] == 0:
                del self.counter[number]
            self.frequency[freq].discard(number)
            if freq > 1:
                self.frequency[freq - 1].add(number)


    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.frequency and len(self.frequency[frequency]) > 0