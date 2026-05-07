class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res=[]

        for v in nums:
            if v==2: res.append(-1)

            for x in range(1001):
                if x|(x+1)==v:
                    res.append(x)
                    break


        return res


        # ans = []

        # for i in nums:
        #     f = True
        #     for v in range(1001):
        #         if (v | (v + 1)) == i:
        #             ans.append(v)
        #             f = False
        #             break

        #     if f: ans.append(-1)


        # return ans