class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # Key insight: if k >= len(arr)-1, the maximum element will win
        # because it will beat every other element at least once
        if k >= len(arr) - 1:
            return max(arr)
        
        current_winner = arr[0]
        consecutive_wins = 0
        
        # Compare current winner with each subsequent element
        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                # Current winner beats arr[i]
                consecutive_wins += 1
            else:
                # arr[i] becomes the new winner
                current_winner = arr[i]
                consecutive_wins = 1  # Reset count, new winner has 1 win
            
            # If current winner has k consecutive wins, return it
            if consecutive_wins == k:
                return current_winner
        
        # If we've gone through all elements and no one got k wins,
        # the current winner (largest element seen) will keep winning
        return current_winner


        
        # d=defaultdict(int)
        # dq=deque(arr)

        # while 1:
        #     if dq[0]>dq[1]:
        #         d[dq[0]]+=1
        #         if d[dq[0]]==k: return dq[0]
        #         tmp=dq.popleft()
        #         dq.rotate(-1)
        #         dq.appendleft(tmp)
        #     else:
        #         d[dq[1]]+=1
        #         if d[dq[1]]==k: return dq[1]
        #         dq.rotate(-1)