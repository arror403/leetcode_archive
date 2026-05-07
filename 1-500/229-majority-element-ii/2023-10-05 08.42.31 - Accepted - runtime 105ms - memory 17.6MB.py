class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # t=int(len(nums)/3)
        # d=Counter(nums).values()
        # print(d)


        return [k for k,v in Counter(nums).items() if v>int(len(nums)/3)]