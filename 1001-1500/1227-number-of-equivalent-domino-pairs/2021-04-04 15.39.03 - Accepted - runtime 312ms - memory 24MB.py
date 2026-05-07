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
                sum+=int(factorial(k)/(2*factorial(k-2)))
            
        # print (d)
            

        return sum
    
    def factorial(self, n:int)->int:
        fact=1
        for i in range(1,n+1):
            fact = fact * i
        return fact
        