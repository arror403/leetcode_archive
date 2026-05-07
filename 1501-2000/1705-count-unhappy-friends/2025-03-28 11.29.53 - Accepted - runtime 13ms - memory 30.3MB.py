class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        m = [[-1]*n for _ in range(n)]
        
        partner = {}
        for x, y in pairs:
            partner[x] = y
            partner[y] = x
        
        # Populate the preference ranking matrix
        for i, friends in enumerate(preferences):
            for rank, friend in enumerate(friends):
                m[i][friend] = rank
        
        # Count unhappy friends
        unhappy = 0
        for x in range(n):
            # Get x's current partner
            y = partner[x]
            
            # Check x's preferences before their current partner
            for u in preferences[x]:
                # Stop if we reach the current partner
                if u == y:
                    break
                
                # Check if x prefers u more than current partner
                # And check if u also prefers x more than their current partner
                if m[x][u] < m[x][y]:
                    v = partner[u]
                    if m[u][x] < m[u][v]:
                        unhappy += 1
                        break
        
        
        return unhappy