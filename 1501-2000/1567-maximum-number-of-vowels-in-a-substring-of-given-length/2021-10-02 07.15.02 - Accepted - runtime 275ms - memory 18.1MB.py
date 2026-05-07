class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        b=[]
        tmp=0
        r=[]
        
        if len(s)==k:
            return k
        else:
            for i in range(len(s)):
                if s[i]=="a" or s[i]=="i" or s[i]=="u" or s[i]=="e" or s[i]=="o":
                    b.append(1)
                else:
                    b.append(0)    

            x = sum(b[:k])
            r.append(x)  

            k-=1 
            while(1):
                k+=1
                if k!=(len(b)-1):
                    x-=b[tmp]
                    tmp+=1
                    x+=b[k]
                    r.append(x)
                else:
                    break

            r.append(x-b[tmp]+b[k])        

            print(r)
            return max(r)