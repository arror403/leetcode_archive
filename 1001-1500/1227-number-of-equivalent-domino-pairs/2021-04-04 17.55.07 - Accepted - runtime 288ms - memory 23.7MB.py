class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        sum=0
        l=0
        b=[]
        d=[]
        for r in dominoes: l+=1
            
        for i in range(l): dominoes[i].sort()
            
        for j in dominoes:
            if not(j in b):
                b.append(j)
                d.append(dominoes.count(j))
            
        for k in d: 
            if k>=2:
                sum+=int((k*(k-1))/2)
            
        # print (d)
            

        return sum

        