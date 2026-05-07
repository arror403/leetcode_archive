class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=list(s)
        b=s[len(s)//2:]
        a=s[:len(s)//2]
        ca,cb=0,0
        # print(a,b)
        for i in b:
            if i=='a' or i=='e' or i=='i'or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                cb+=1
        for i in a:
            if i=='a' or i=='e' or i=='i'or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                ca+=1

        return ca==cb