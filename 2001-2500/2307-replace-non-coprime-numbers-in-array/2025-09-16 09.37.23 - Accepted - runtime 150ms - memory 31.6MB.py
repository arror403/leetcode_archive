class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            res.append(n)
            while len(res) > 1 and gcd(res[-1], res[-2]) > 1:
                res.append(lcm(res.pop(), res.pop()))


        return res

        # def primeFactors(n):
        #     p=set([1])
        #     # number of two's that divide n
        #     while n % 2 == 0:
        #         p.add(2)
        #         n //= 2
                
        #     # n must be odd at this point so a skip of 2 ( i+=2) can be used
        #     for i in range(3, int(sqrt(n))+1, 2):
        #         # while i divides n , print i and divide n
        #         while n % i== 0:
        #             p.add(i)
        #             n //= i
                    
        #     # Condition if n is a prime number greater than 2
        #     if n > 2: p.add(n)

        #     return p
        
        # d={n:primeFactors(n) for n in nums}
        # q=deque(nums)

        # while 1:
        #     L=len(q)
        #     f=1
        #     for i in range(L-1):
        #         if q[i] not in d: d[q[i]]=primeFactors(q[i])
        #         if q[i+1] not in d: d[q[i+1]]=primeFactors(q[i+1])
        #         # print(q[i], q[i+1], d[q[i]] & d[q[i+1]])
        #         if d[q[i]] & d[q[i+1]] != set([1]):
        #             f=0
        #             # a, b = q.popleft(), q.popleft()
        #             q.insert(i,lcm(q[i],q[i+1]))
        #             break
        #     print(q)
            
        #     if f: return list(q)


        # return [0]