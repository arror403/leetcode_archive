class Solution:
    def findNthDigit(self, n: int) -> int:
        r=[[1,9],[10,189],[190,2889],[2890,38889],[38890,488889],[488890,5888889],[5888890,68888889],[68888890,788888889],[788888890,2147483647]]

        for i,v in enumerate(r):
            if n>=v[0] and n<=v[1]:
                p=i
                break

        a,b=divmod((n-r[p][0]),(p+1))

        a+=10**p

        return int(str(a)[b])