class Solution:
    def maxOperations(self, s: str) -> int:
        pref = list(accumulate(int(c) for c in s))
        return sum({pref[i] for i,c in enumerate(s) if c=='0'})
        # L=len(s)
        # s=list(s)
        # S=sorted(s)
        # res=0
        # f=p=True


        # while 1:
        #     for i in range(L-1):
        #         f=True
        #         if s[i]=='1' and s[i+1]=='0':
        #             f=False
        #             p=True
        #             s[i]='0'
        #             for j in range(i+2, L):
        #                 if s[j]=='1':
        #                     p=False
        #                     s[j-1]='1'
        #                     res+=1
        #                     break
        #         # print(s)
        #         # print(f,p)
        #         if f and p:break        

        #     print(res)
        #     if s==S: return res