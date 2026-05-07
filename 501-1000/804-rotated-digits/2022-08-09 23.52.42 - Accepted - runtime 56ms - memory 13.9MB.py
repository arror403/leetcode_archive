class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotated_same_nums = set([0, 1, 8])
        rotated_valid_nums = set([0, 1, 8, 2, 5, 6, 9])
        nums = set()
        result = 0
        digits = list(map(int, str(n)))
        for i, digit in enumerate(digits):
            for num in range(digit):
                if nums.issubset(rotated_valid_nums) and num in rotated_valid_nums:
                    result += 7**(len(digits) - i - 1)
                if nums.issubset(rotated_same_nums) and num in rotated_same_nums:
                    result -= 3**(len(digits) - i - 1)
            if digit not in rotated_valid_nums:
                return result
            nums.add(digit)
        return result + (nums.issubset(rotated_valid_nums) and not nums.issubset(rotated_same_nums))
#         res=0
#         for i in range(1,n+1):
#             tmp=i
#             i=self.tolist(i)
#             if 3 in i or 4 in i or 7 in i: continue
#             for j in range(len(i)):
#                 if i[j]==2: i[j]=5
#                 elif i[j]==5: i[j]=2
#                 elif i[j]==6: i[j]=9
#                 elif i[j]==9: i[j]=6
#             i=int(''.join([str(x) for x in i]))
#             # print(i,tmp)
#             if i!=tmp: res+=1
                
#         return res
        
        
#     def tolist(self, x):
#         return list(map(int,str(x)))