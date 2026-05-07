class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res=0
        # s=set()

        for i in range(num1, num2+1):
            t=list(map(int,str(i)))
            for j in range(1, len(t)-1):
                if t[j]>t[j+1] and t[j]>t[j-1]:
                    res+=1
                    # s.add((t[j-1], t[j], t[j+1]))
                if t[j]<t[j+1] and t[j]<t[j-1]:
                    res+=1
                    # s.add((t[j-1], t[j], t[j+1]))

        # print(s)
        return res