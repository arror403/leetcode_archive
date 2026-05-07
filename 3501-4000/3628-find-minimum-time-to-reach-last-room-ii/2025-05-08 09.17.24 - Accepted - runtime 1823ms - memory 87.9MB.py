class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        totalRows,totalCols=len(moveTime),len(moveTime[0])
        adjacentDirections=[(1,0), (-1,0), (0,1), (0,-1)]
        pq=[[0,0,0,1]]
        heapq.heapify(pq)
        minimumArrivalTime=[[inf]*totalCols for _ in range(totalRows)]
        minimumArrivalTime[0][0]=0

        while pq:
            currentTime, currentRow, currentCol, currentStepCost = heapq.heappop(pq)

            # If we reached the target room (totalRows - 1, totalCols - 1)
            if (currentRow==totalRows-1 and currentCol==totalCols-1):
                return currentTime
            
            # Explore adjacent rooms
            for dx,dy in adjacentDirections:
                nextRow = currentRow + dx
                nextCol = currentCol + dy

                if (nextRow>=0 and nextRow<totalRows and nextCol>=0 and nextCol<totalCols):
                    waitTime=max(moveTime[nextRow][nextCol]-currentTime, 0)
                    newArrivalTime=currentTime+currentStepCost+waitTime

                    # Only push to the queue if we found a better arrival time
                    if (newArrivalTime < minimumArrivalTime[nextRow][nextCol]):
                        minimumArrivalTime[nextRow][nextCol] = newArrivalTime
                        nextStepCost=1 if currentStepCost==2 else 2
                        heapq.heappush(pq, [newArrivalTime, nextRow, nextCol, nextStepCost])


        return -1