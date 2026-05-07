class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = {}  # To store the frequency of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
            
        max_heap = []  # Priority queue to store characters based on their frequency
        for char, count in char_count.items():
            heapq.heappush(max_heap, (-count, char))  # Using negative count to create a max heap
            
        prev_char = None
        result = []
        
        while max_heap:
            neg_count, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_char:
                heapq.heappush(max_heap, (prev_char[0], prev_char[1]))  # Push back the previous character
            if neg_count + 1 < 0:
                prev_char = (neg_count + 1, char)  # Save the current character for the next iteration
            else:
                prev_char = None
            
        if len(result) != len(s):
            return ""  # Not possible to rearrange
            
        return ''.join(result)