class Solution:
    def countCollisions(self, dir: str) -> int:
        res=0
        i=0
        carsFromRight=0
        L=len(dir)
        
        while (i<L and dir[i]=='L'): i+=1 # skipping all the cars going to left from beginning
        
        for j in range(i, L):
            if dir[j]=='R': 
                carsFromRight+=1
            else:
                # if dir[i] == 'S' then there will be carsFromRight number of collission
                # if dir[i] == 'L' then there will be carsFromRight+1 number of collision (one collision for the rightmost cars and carsFromRight collision for the cars coming from left)
                res += carsFromRight if dir[j]=='S' else carsFromRight+1
                carsFromRight = 0
            
        
        return res


        # res=0
        # d=deque(directions)

        # while 1:
        #     if d[0]=='L': d.popleft()
        #     else: break

        # while 1:
        #     if d[-1]=='R': d.pop()
        #     else: break