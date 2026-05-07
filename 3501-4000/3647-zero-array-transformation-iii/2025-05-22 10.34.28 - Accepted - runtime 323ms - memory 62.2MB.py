class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        candidate=[]
        chosen=[]
        res = j = 0

        for i in range(len(nums)):
            while j<len(queries) and queries[j][0]==i:
                heappush(candidate, -queries[j][1])
                j+=1

            nums[i]-=len(chosen)

            while (nums[i]>0 and candidate and -candidate[0]>=i):
                res+=1
                heappush(chosen, -candidate[0])
                heappop(candidate)
                nums[i]-=1

            if nums[i]>0:
                return -1

            while (chosen and chosen[0]==i):
                heappop(chosen)
            

        return len(queries)-res