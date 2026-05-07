class Solution:
    def reverseVowels(self, s: str) -> str:
        t,res=[],[]
        v=["a","e","i","o","u","A","E","I","O","U"]
        for i in s:
            if i in v:
                t.append(i)
        t.reverse()
        x=0
        for i in s:
            if i in v:
                res.append(t[x])
                x+=1
            else:
                res.append(i)

        return ''.join(res)