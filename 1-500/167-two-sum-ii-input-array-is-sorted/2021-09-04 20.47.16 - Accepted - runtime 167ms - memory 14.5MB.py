class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tmp = 0
        c=0
        b=[]
        
        a=[]
        ai=[]
        index=0
        for i in numbers:
            if i==target/2:
                c+=1
        
        if (target in numbers) and (0 in numbers):
            for i in range(len(numbers)):
                if numbers[i]==0:
                    b.append(i+1)
                elif numbers[i]==target:
                    b.append(i+1)
        elif c>=2:
            for i in range(len(numbers)):
                if(target/2==numbers[i]):
                    b.append(i+1)
                    b.append(i+2)
                    break
        else:
            for i in numbers:
                index+=1
                if not i in a:
                    a.append(i) 
                    ai.append(index)

            # print (a)


            for i in range(len(a)):
                for j in range(i,len(a)):
                    if (a[i]+a[j])==target and i!=j:
                        b.append(ai[i])
                        b.append(ai[j])
                        break
                        
        return b
                    