class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quick_sort(nums)


    def quick_sort(self, l):
        if len(l)<2: return l

        left,right,piv = [],[],[]
        pivot = random.choice(l)

        for v in l:
            if v==pivot:  piv.append(v)
            elif v<pivot: left.append(v)
            else:         right.append(v)

        return self.quick_sort(left) + piv + self.quick_sort(right)