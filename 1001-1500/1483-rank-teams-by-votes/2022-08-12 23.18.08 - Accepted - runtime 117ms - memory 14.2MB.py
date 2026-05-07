class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = {v: [0] * len(votes[0]) + [v] for v in votes[0]}
        # print(count)
        for vote in votes:
            for i, v in enumerate(vote):
                # print(v,i)
                count[v][i] -= 1
        # print(count)
        # print(votes[0])
        return ''.join(sorted(votes[0], key=count.get))
    
    

#         res=''
#         d=dict.fromkeys(string.ascii_uppercase, 0)
#         for i in votes:
#             for j in range(len(i)):
#                 d[i[j]]+=(j+1)
                
#         d=dict(sorted(d.items(), key=lambda item: item[1]))
#         print(d)
        
#         for i in d:
#             if d[i]!=0:
#                 res+=i
#         return res