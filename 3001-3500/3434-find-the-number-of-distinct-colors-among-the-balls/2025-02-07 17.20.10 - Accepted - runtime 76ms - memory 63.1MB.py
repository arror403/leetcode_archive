class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        counts = defaultdict(int)
        result = []
        
        for idx, new_color in queries:
            if idx in colors:
                old_color = colors[idx]
                counts[old_color] -= 1
                if counts[old_color] == 0:
                    del counts[old_color]
            
            colors[idx] = new_color
            counts[new_color] += 1
            result.append(len(counts))
            
        return result