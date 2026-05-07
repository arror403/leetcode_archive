class Solution:
    def minChanges(self, n: int, k: int) -> int:
        bin_n=bin(n)[2:]
        bin_k=bin(k)[2:]
        res=0
        
        if len(bin_n)<len(bin_k): return -1  # Impossible case: n has fewer bits than k
        
        bin_k=bin_k.zfill(len(bin_n))
        
        for a,b in zip(bin_n, bin_k):
            if a=='1' and b=='0': res+=1
            elif a=='0' and b=='1': return -1  # Impossible to change 0 to 1
        
        return res


        
        # if n==k: return 0

        # res=0
        # r=bin(n^k)[2:]
        # n=bin(n)[2:]

        # if len(r)<len(n): r=r.zfill(len(n)-len(r))
        # print(r,n)

        # for a,b in zip(r,n):
        #     if a==b=='1': res+=1
        #     elif a=='1' and b=='0': return -1
            

        # return res