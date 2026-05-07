class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        t=0
        b=self.sub_lists(arr)
        for i in b:
            if len(i)%2==1:
                t+=sum(i)
                
        return t 
        

    def sub_lists (self,l):
        lists = [[]]
        for i in range(len(l) + 1):
            for j in range(i):
                lists.append(l[j: i])
        return lists