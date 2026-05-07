class Solution:
    def secondHighest(self, s: str) -> int:
        # m=[i.isnumeric() for i in list(s)]
        m=[]
        for i in list(s):
            if i.isnumeric():
                m.append(i)
        m=list(set(m))

        return sorted(m)[-2] if len(m)>=2 else -1