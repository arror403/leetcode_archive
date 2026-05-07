class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        nextLetter={'a':'bc', 'b':'ac', 'c':'ab'} 
        d=deque(['a', 'b', 'c'])
        
        while len(d[0])!=n:
            u=d.popleft()
            for v in nextLetter[u[-1]]:
                d.append(u+v)


        return d[k-1] if len(d)>=k else ""