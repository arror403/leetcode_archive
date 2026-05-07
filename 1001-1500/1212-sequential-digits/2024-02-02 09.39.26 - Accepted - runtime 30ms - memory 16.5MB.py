class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        ##### improved by chatGPT #####

        m = '123456789'
        l = len(str(low))
        h = len(str(high))
        res = []

        for i in range(l, h + 1):
            for j in range(10 - i):
                num_str = m[j:j+i]
                num = int(num_str)
                if low <= num <= high:
                    res.append(num)
                    
        return sorted(res)