class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        max_prime = 0
        
        for i in range(n):
            if self.is_prime(nums[i][i]):
                max_prime = max(max_prime, nums[i][i])
            if self.is_prime(nums[i][n - i - 1]):
                max_prime = max(max_prime, nums[i][n - i - 1])

        return max_prime

    def is_prime(self, number):
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for num in range(3, int(number ** 0.5) + 1, 2):
            if number % num == 0:
                return False
        return True