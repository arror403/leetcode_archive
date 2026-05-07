class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c=Counter(moves)
        return max((c['L']+c['_']-c['R']),(c['R']+c['_']-c['L']))