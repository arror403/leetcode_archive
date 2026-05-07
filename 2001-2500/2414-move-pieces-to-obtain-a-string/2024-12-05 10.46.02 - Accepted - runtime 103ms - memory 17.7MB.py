class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # p=''.join([c for c in start if c!="_"])
        # q=''.join([c for c in target if c!="_"])

        # if p!=q: return False

        # d=defaultdict(list)

        # for i,c in enumerate(start): d[c].append(i)
        # # print(d)

        # if len(d['_'])>=len(d['L']) and 

        # return True
        n=len(target)
        i=j=0

        while i<=n and j<=n:
            while i<n and target[i]=='_':
                i+=1
            while j<n and start[j]=='_':
                j+=1
            if i==n or j==n: 
                return i==j==n
            
            if target[i]!=start[j]: 
                return False
            if target[i]=='L':
                if j<i: return False
            
            else:
                if i<j: return False

            i+=1
            j+=1


        return True