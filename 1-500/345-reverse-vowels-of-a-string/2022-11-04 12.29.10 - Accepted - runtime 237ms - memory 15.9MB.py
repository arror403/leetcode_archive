class Solution:
    def reverseVowels(self, s: str) -> str:
        t,res=[],[]
        for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                t.append(i)
        t.reverse()
        x=0
        for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                res.append(t[x])
                x+=1
            else:
                res.append(i)

        return ''.join(res)