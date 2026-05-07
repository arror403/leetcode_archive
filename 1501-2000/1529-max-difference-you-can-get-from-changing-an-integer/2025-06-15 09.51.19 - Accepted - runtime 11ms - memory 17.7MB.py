class Solution:
    def maxDiff(self, num: int) -> int:
        nums=list(str(num))
        m=set()
        m.add(num)

        for a in range(10):
            for b in range(10):
                if a==b or str(a) not in nums: continue
                # print(a,b)
                tmp=[str(b) if x==str(a) else x for x in nums]
                if tmp[0]!='0': m.add(int(''.join(tmp)))
                # print(int(''.join(tmp)))

        if 0 in m: m.remove(0)
        m=list(m)
        # print(m)

        return max(m)-min(m)