class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n+1)

        for a,b,s in bookings:
            res[a-1] += s
            res[b] -= s

        # Convert difference array to actual values
        for i in range(1, n):
            res[i]+=res[i-1]


        return res[:n]