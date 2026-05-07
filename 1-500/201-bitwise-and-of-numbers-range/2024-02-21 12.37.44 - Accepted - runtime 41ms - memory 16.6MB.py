class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        shift=0
        # find the common prefix
        while l<r:
            l>>=1
            r>>=1
            shift+=1
        return l<<shift

        # if l==r: return r
        # n=bin(l)[2:]
        # m=bin(r)[2:]
        # L=len(m)
        # if len(n)!=L: return 0
        
        # res=0

        # for i in range(L):
        #     if m[i]=='1' and n[i]=='1':
        #         res+=1
        #     else:
        #         break

        # print(m,n,res,L)

        # return int(res*'1'+(L-res)*'0',2)


        # if l==0: return 0
        # t=int(log2(l))
        # return 2**t if t==int(log2(r)) else 0