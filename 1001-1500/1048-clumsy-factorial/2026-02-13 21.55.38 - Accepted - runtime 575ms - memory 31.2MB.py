class Solution:
    def clumsy(self, n: int) -> int:
        # return 0
        s = ''
        op = ['*', '//', '+', '-']
        i = 0
        for j in range(n, 0, -1):
            s += str(j)
            if j != 1:
                s += op[i]
            i = (i+1)%4

        # print(s)

        return eval(s)