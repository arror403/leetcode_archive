class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        d = Counter(digits)
        res = []
        
        for num in range(100, 999, 2):
            valid = True
            for v,f in Counter(int(x) for x in str(num)).items():
                if d[v] < f:
                    valid = False
                    break
            
            if valid: res.append(num)
                

        return res