class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n=len(nums)
        if value==1: return n

        freq=[0]*value
        for item in nums: freq[item%value]+=1

        maxround=min(freq)
        freq=[item-maxround for item in freq]
        if freq[0]==0: return maxround*value

        ind=0
        while ind+1<value and freq[ind+1]>0: ind+=1


        return maxround*value+ind+1



        # m = [x%value if x>0 else ceil(abs(x)/value)*value+x for x in nums]
        # d = sorted(Counter(m).items(), key = lambda x: x[0])
        # s = set()

        # for v,f in d:
        #     for p in range(f):
        #         s.add(v+value*p)

        # res = 0
        # while 1:
        #     if res in s:
        #         res+=1
        #     else:
        #         return res