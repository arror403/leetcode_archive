class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # L = len(nums)
        # nums.sort()
        # res = 0

        # for a, b in combinations(nums, 2):
        #     print(a, b, bisect_left(nums, a+b))
        #     res+=L-bisect_left(nums, a+b)

        # return res

        L = len(nums)
        nums.sort()
        res = 0

        def binarySearch(l, r, x):
            while r >= l and r < L:
                mid = (l + r) // 2
                if nums[mid] >= x:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        for i in range(L-2):
            k = i + 2
            for j in range(i + 1, L - 1):
                if nums[i] == 0: continue
                k = binarySearch(k, L - 1, nums[i] + nums[j])
                res += k - j - 1


        return res

# public class Solution {
#     public int triangleNumber(int[] nums) {
#         int count = 0;
#         Arrays.sort(nums);
#         for (int i = 0; i < nums.length - 2; i++) {
#             int k = i + 2;
#             for (int j = i + 1; j < nums.length - 1 && nums[i] != 0; j++) {
#                 while (k < nums.length && nums[i] + nums[j] > nums[k])
#                     k++;
#                 count += k - j - 1;
#             }
#         }
#         return count;
#     }
# }