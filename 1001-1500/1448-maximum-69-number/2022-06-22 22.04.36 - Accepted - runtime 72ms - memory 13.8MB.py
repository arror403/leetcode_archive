class Solution:
    def maximum69Number (self, num: int) -> int:
        t=list(map(int,str(num)))
        for i in range(len(t)):
            if t[i]==9:
                continue
            elif t[i]==6:
                t[i]=9
                break
        s = [str(i) for i in t]
        a_string = "".join(s)
        res = int(a_string)
        return res