class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        res=meetings[0][0]-1
        L=len(meetings)

        for i in range(1, L):
            if meetings[i][0]<=meetings[i-1][1]:
                if meetings[i][1]<meetings[i-1][1]:
                    meetings[i][1]=meetings[i-1][1]
            else:
                res+=meetings[i][0]-meetings[i-1][1]-1

        res+=days-meetings[L-1][1]


        return res