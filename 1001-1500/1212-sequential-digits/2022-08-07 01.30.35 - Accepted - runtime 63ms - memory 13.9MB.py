class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        m=['1','2','3','4','5','6','7','8','9']
        l,h,res=len(str(low)),len(str(high)),[]
        for i in range(l,h+1):
            for j in range(10):
                if i+j>9: break
                else:
                    tmp=m[j:i+j]
                    # tmp=[str(x) for x in tmp]
                    tmp=''.join(tmp)
                    tmp=int(tmp)
                    if low<=tmp<=high:
                        res.append(tmp)
                    
        return sorted(res)