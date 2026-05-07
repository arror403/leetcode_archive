class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count={v: [0]*len(votes[0]) + [v] for v in votes[0]}
        for v in votes:
            for i, v in enumerate(v):
                count[v][i]-=1
            
        return ''.join([i for i in dict(sorted(count.items(), key=lambda item: item[1]))])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         count = {v: [0] * len(votes[0]) + [v] for v in votes[0]}
#         for vote in votes:
#             for i, v in enumerate(vote):
#                 # print(v,i)
#                 count[v][i] -= 1
                
#         # print(count)
        
#         # print(dict(sorted(count.items(), key=lambda item: item[1])))
#         return ''.join([i for i in dict(sorted(count.items(), key=lambda item: item[1]))])