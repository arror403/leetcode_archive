class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_len = 0
        curr_sum = 0
        start = 0
        L=len(s)
        d=[abs(ord(s[i])-ord(t[i])) for i in range(L)]

        for end in range(L):
            curr_sum+=d[end]

            while curr_sum>maxCost:
                curr_sum-=d[start]
                start+=1

            max_len=max(max_len, end-start+1)

        return max_len