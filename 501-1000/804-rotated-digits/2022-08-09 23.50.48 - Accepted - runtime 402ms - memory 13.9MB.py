class Solution:
    def rotatedDigits(self, n: int) -> int:
        res=0
        for i in range(1,n+1):
            tmp=i
            i=self.tolist(i)
            if 3 in i or 4 in i or 7 in i: continue
            for j in range(len(i)):
                if i[j]==2: i[j]=5
                elif i[j]==5: i[j]=2
                elif i[j]==6: i[j]=9
                elif i[j]==9: i[j]=6
            i=int(''.join([str(x) for x in i]))
            # print(i,tmp)
            if i!=tmp: res+=1
                
        return res
        
        
    def tolist(self, x):
        return list(map(int,str(x)))