class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = []
        res = [0]*n
        ready = [i for i in range(n)]
        heapify(ready)

        for a,b in meetings:
            while rooms and rooms[0][0]<=a:
                _,r = heappop(rooms)
                heappush(ready, r)
            if ready:
                r = heappop(ready)
                heappush(rooms, [b, r])
            else:
                t,r = heappop(rooms)
                heappush(rooms, [t+b-a, r])

            res[r]+=1


        return next(i for i,v in enumerate(res) if v==max(res))