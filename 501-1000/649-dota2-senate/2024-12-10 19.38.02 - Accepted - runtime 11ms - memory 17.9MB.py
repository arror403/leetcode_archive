class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad=deque()
        d=deque()
        n=len(senate)

        # Add all senators to respect queue with index
        for i in range(n):
            if senate[i]=='R':
                rad.append(i)
            else:
                d.append(i)

        # Use increasing n to keep track of position
        while rad and d:
            # Only "winner" stays in their queue
            if rad[0]<d[0]:
                rad.append(n)
                n+=1
            else:
                d.append(n)
                n+=1
            
            rad.popleft()
            d.popleft()


        return "Radiant" if rad else "Dire"