class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=Counter([i[0] for i in matches])
        losers=Counter([i[1] for i in matches])
        return [sorted(winners.keys()-losers.keys()),sorted(k for k,v in losers.items() if v==1)]