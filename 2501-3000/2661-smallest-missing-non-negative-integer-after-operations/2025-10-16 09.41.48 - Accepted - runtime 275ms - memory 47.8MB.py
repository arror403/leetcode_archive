class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        m = [x%value if x>0 else ceil(abs(x)/value)*value+x for x in nums]
        # print(m)
        d = sorted(Counter(m).items(), key = lambda x: x[0])
        s = set()

        for v,f in d:
            for p in range(f):
                s.add(v+value*p)

        # print(s)
        res = 0
        while 1:
            if res in s:
                res+=1
            else:
                return res


        return 77885566