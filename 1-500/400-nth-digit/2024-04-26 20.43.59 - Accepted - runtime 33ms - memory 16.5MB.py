class Solution:
    ##### power by chatGPT #####
    def findNthDigit(self, n: int) -> int:
        # Length of the numbers with d digits
        length = 1
        # Number of numbers with d digits
        count = 9
        # Start with one-digit numbers
        start = 1

        # Find the length of the number that contains the nth digit
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        # Find the actual number that contains the nth digit
        start += (n - 1) // length

        # Find the nth digit within the number
        return int(str(start)[(n - 1) % length])