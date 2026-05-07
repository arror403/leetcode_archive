class FreqStack:

    ##### power by chatGPT #####

    def __init__(self):
        self.freq_counter = defaultdict(int)
        self.grouped_elements = defaultdict(list)
        self.max_heap = []

    def push(self, x: int) -> None:
        freq = self.freq_counter[x] + 1
        self.freq_counter[x] = freq
        heapq.heappush(self.max_heap, (-freq, -len(self.grouped_elements[freq]), x))
        self.grouped_elements[freq].append(x)

    def pop(self) -> int:
        if self.max_heap:
            _, _, element = heapq.heappop(self.max_heap)
            freq = self.freq_counter[element]
            self.grouped_elements[freq].pop()
            if not self.grouped_elements[freq]:
                del self.grouped_elements[freq]
            self.freq_counter[element] -= 1
            return element