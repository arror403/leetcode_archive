class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp=[0]*(n+1)
        dp[1]=1
        share=res=0
        mod=10**9+7

        for i in range(2, n+1):
            share=(share+dp[max(i-delay, 0)]-dp[max(i-forget, 0)]+mod)%mod
            dp[i]=share
        
        for i in range(n-forget+1, n+1):
            res=(res+dp[i])%mod
        
        
        return res
        


        # p=[1]
        
        # i=0
        # while i<n:
        #     print(p)
        #     f=1
        #     for x in range(len(p)):
        #         if (forget+x)<=i:
        #             p[x]=0
                
        #         if f and (delay+x)>=i and p[x]:
        #             p.append(1)
        #             f=0

        #     i+=1


        # return 0