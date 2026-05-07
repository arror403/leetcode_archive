class Solution:
    def maxSum(self, nums: List[int]) -> int:

        def max_digit(n):
            tmp=list(map(int,str(n)))
            return max(tmp)

        m=sorted([[v,max_digit(v)] for v in nums],key=lambda x:x[1])
            

        t=[list(g) for _,g in groupby(m,key=lambda x:x[1])]


        # return max([sum(nlargest(2, [x[0] for x in i])) for i in t if len(i)>1],-1)
        max_sum = -1
        for i in t:
            if len(i)>1:
                sum_of_two_largest = sum(nlargest(2, [x[0] for x in i]))
                max_sum = max(max_sum, sum_of_two_largest)

        return max_sum
            