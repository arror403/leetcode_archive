class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        d=deque(colors)
        d.append(colors[0])
        d.appendleft(colors[-1])
        return sum(1 for i in range(1,len(d)-1) if [d[i-1],d[i],d[i+1]] in [[0,1,0],[1,0,1]])