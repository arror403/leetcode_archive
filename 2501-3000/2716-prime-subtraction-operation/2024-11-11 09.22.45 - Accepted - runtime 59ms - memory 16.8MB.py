class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n=len(nums)
        prime=[]
        res=0
        isPrime=[True]*1005
        isPrime[0]=isPrime[1]=False

        i=2
        while(i**2<1005):
            for j in range(2*i,1005,i):
                isPrime[j]=False
            i+=1
        
        for i in range(1004):
            if isPrime[i]: prime.append(i)
        
        prev=nums[-1]
        for i in range(n-2,-1,-1):
            if nums[i]<prev:
                prev=nums[i]
                continue
            res=1

            sub=0
            while(sub<len(prime) and prime[sub]<nums[i]):
                if(nums[i]-prime[sub]<prev):
                    prev = nums[i]-prime[sub]
                    res=0
                    break
                sub+=1

            if res: break


        return not res