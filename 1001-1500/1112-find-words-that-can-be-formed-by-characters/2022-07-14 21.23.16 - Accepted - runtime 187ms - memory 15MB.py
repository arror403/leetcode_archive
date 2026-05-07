class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        m=[0]*26
        for i in chars: m[ord(i)-97]+=1
        words=[list(i) for i in words]
        chars=list(chars)
        t=0

        for i in words:
            # print("m:  ",m)
            tmp=list(m)
            f=1
            for j in i:
                if tmp[ord(j)-97]>0:
                    tmp[ord(j)-97]-=1
                    continue
                else:
                    f=0
                    break
            if f:
                t+=len(i)
            # print("tmp:",tmp)

        return (t)