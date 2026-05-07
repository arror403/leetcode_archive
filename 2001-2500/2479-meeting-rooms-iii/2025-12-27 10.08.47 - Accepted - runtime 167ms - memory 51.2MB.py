class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time so we process them in order
        meetings.sort()
        # Heap to track busy rooms: [end_time, room_number]
        rooms = []
        # Count how many meetings each room has hosted
        res = [0] * n
        # Heap of available room numbers (lower numbers have priority)
        ready = [i for i in range(n)]
        heapify(ready)

        for a, b in meetings:  # a = start time, b = end time
            # Step 1: Free up any rooms whose meetings have ended by time 'a'
            while rooms and rooms[0][0] <= a:
                _, r = heappop(rooms)      # Get the room that finished
                heappush(ready, r)          # Mark it as available again
            # Step 2: Assign the current meeting to a room
            if ready:
                # Case A: There's a free room available
                r = heappop(ready)          # Take the lowest numbered free room
                heappush(rooms, [b, r])     # Room is busy until time 'b'
            else:
                # Case B: No free rooms, must wait for the earliest one to finish
                t, r = heappop(rooms)       # Get room that finishes soonest
                heappush(rooms, [t + b - a, r])  # Delay meeting: new end = old end + meeting duration
            # Step 3: Count this meeting for the assigned room
            res[r] += 1

        # Return the room with the most meetings (smallest index if tie)
        return next(i for i, v in enumerate(res) if v == max(res))