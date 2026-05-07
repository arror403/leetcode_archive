class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        m=['1','2','3','4','5','6','7','8','9']
        l=len(str(low))
        h=len(str(high))
        res=[]

        for i in range(l,h+1):
            for j in range(10):
                if i+j>9: break
                else:
                    tmp=int(''.join(m[j:i+j]))
                    if low<=tmp and tmp<=high:
                        res.append(tmp)
                    
        return sorted(res)