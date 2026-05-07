class Solution:
    def numSquares(self, n: int) -> int:
        def isSquare(x):
            sqRoot = int(math.sqrt(x))
            return (sqRoot * sqRoot == x)
        
        # Function to count minimum squares that sum to n
        def cntSquares(n):
        
            # ans = 1 if the number is a perfect square
            if (isSquare(n)):
                return 1
            
            # ans = 2:
            # we check for each i if n - (i * i) is a perfect
            # square
            for i in range(1, int(math.sqrt(n))+1):
                if (isSquare(n - (i * i))):
                    return 2
                
            # ans = 4
            # possible if the number is representable in the form
            # 4^a (8*b + 7).
            while (n % 4 == 0):
                n >>= 2
            
            if (n % 8 == 7):
                return 4
            
            # since all the other cases have been evaluated, the
            # answer can only then be 3 if the program reaches here
            return 3
        return cntSquares(n)