class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        b=[]
        for i in arr:
            if i%2==1:
                b.append(1)
            else:
                b.append(0)
                
        if len(b)<3:
            return 0
        else:
            for i in range(1,len(b)-1):
                if b[i-1]==b[i]==b[i+1]==1:
                    return 1