class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        a=[0]*26
        b=[0]*26
        m=[]
        for i in s: a[ord(i)-97]+=1
        for i in target: b[ord(i)-97]+=1
        for i in range(26):
            if b[i]==0: continue
            else: m.append(int(a[i]/b[i]))

        return min(m)