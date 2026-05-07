class Solution:
    def judgeSquareSum(self, n: int) -> bool:
        if n==1 or n==0 : return True

        s = dict()
        for i in range(n):

            if i*i > n:
                break
            # store square value in hashmap
            s[i*i] = 1

            if (n - i*i) in s.keys():
                # print((n - i * i)**(1 / 2), "^2 +", i, "^2")
                return True

        return False