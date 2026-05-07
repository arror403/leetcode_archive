class Solution:
    def reinitializePermutation(self, n: int) -> int:
#         p=[]
#         arr=[]
#         for i in range(n):
#             p.append(i)
        
#         for i in range(n):
#             if (i%2)==0:
#                 arr.append(p[int(i/2)])
#             elif (i%2)==1:
#                 arr.append(p[int((n/2)+(i-1)/2)])
#         print (p)    
#         print (arr)
        i=n/2
        res=1
        while i!=1:
            if i%2 == 0:
                i/=2
            else:
                i=n/2+(i-1)/2
            res+=1
        return res


        #8>3 10>6 12>10 14>12 16>4 18>8 20>18 22>6 24>11 26>20
        #100>30