class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]

        w=list(set(nums))
        count=[]
        for i in w:
            tmp=[i,nums.count(i)]
            count.append(tmp)

        count.sort(key=lambda row: (row[1]), reverse=True)

        # print(count)    
        for i in range(k):
            res.append(count[i][0])
            
        return res