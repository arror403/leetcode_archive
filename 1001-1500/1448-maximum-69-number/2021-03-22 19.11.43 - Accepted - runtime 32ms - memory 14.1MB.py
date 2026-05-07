class Solution:
    def maximum69Number (self, num: int) -> int:
        
        res = [int(x) for x in str(num)] 
        
        s=''
        
        for i in range(0,len(res)):
            if res[i]==6:
                res[i]=9
                break
        for j in res:
            s+=str(j)

        return (s)