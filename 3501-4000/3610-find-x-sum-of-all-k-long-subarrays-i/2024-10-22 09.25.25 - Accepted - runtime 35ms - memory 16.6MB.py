class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def do_sum(i):
            ctr=Counter(nums[i:i+k])
            most_freq=nlargest(x, ctr, key=lambda y: (ctr[y], y))

            return sum(map(lambda y: y*ctr[y], most_freq))


        return list(map(do_sum, range(len(nums)-k+1)))



        # L=len(nums)
        # res=[]
        # for i in range(L-k+1):
        #     print(nums[i:i+k+1])
        #     d=[[v,f] for v,f in Counter(nums[i:i+k+1]).items() if f>=x]
        #     print(d)

        #     res.append(sum([a*b for a,b in d]))


        # return res