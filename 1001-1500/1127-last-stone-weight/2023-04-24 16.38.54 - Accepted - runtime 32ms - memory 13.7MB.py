import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]  # Convert stones to negative numbers and add to heap
        heapq.heapify(heap)  # Heapify the list
        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)  # Get the two largest stones
            if x != y:
                heapq.heappush(heap, -(x - y))  # Add the difference back to the heap
        return -heap[0] if heap else 0  # Return the last stone weight or 0 if the heap is empty