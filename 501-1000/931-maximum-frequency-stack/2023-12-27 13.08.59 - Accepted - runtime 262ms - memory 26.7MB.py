class FreqStack:

    ##### power by chatGPT #####

    def __init__(self):
        self.freq_counter = defaultdict(int)
        self.max_heap = []
        self.index = 0

    def push(self, x: int) -> None:
        freq = self.freq_counter[x] + 1
        self.freq_counter[x] = freq
        heapq.heappush(self.max_heap, (-freq, -self.index, x))
        self.index += 1

    def pop(self) -> int:
        if self.max_heap:
            _, _, element = heapq.heappop(self.max_heap)
            self.freq_counter[element] -= 1
            return element