class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        d = deque(bits)
        
        while len(d) >= 2:
            if d[0] == 0:
                d.popleft()
            else:
                if len(d) < 2: return False
                d.popleft()
                d.popleft()
        

        return d==deque([0])