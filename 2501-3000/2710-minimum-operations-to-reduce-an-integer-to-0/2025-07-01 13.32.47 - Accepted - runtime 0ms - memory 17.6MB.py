class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0

        while n > 0:
            if n & 1 == 0:
                # If rightmost bit is 0, just shift (divide by 2)
                n >>= 1
            else:
                if n & 3 == 3:  # Check if last two bits are 11
                    # If we have consecutive 1s, it's better to add 1
                    # This will create a carry and potentially merge groups
                    n += 1
                    operations += 1
                else:
                    # If it's an isolated 1, subtract it
                    n -= 1
                    operations += 1
        
        
        return operations


        # b=bin(n)[2:]
        # l_b=list(b)
        # res=0

        # print(b)
        # for i in range(1,len(b)-1):
        #     if b[i-1]==b[i+1]=='1' and b[i]=='0':
        #         l_b[i]='1'
        #         res+=1

        # for k,g in groupby(l_b):
        #     if k=='1':
        #         if len(list(g))>1:
        #             res+=2
        #         else:
        #             res+=1
            

        # return res