class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        s = []
        for i in range(n):
            if asteroids[i] > 0 or not s:
                s.append(asteroids[i])
            else:
                while s and s[-1] > 0 and s[-1] < abs(asteroids[i]):
                    s.pop()
                
                if s and s[-1] == abs(asteroids[i]):
                    s.pop()
                
                else:
                    if not s or s[-1] < 0:
                        s.append(asteroids[i])
 
        res = [0] * len(s)
        for i in range(len(s) - 1, -1, -1):
            res[i] = s[-1]
            s.pop()


        return res