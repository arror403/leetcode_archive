class Solution:
    def nearestExit(self, maze: List[List[str]], e: List[int]) -> int:
        q=deque()
        q.append([e[0],e[1]])
		# current moves
        moves=1
        rows,cols=len(maze),len(maze[0])
		# to move in all directions
        offsets=[[0,1],[1,0],[0,-1],[-1,0]]
        # mark the entrance as visited
        maze[e[0]][e[1]]='+'

        while q:
            l=len(q)
			# for every node in the queue visit all of it's adjacent nodes which are not visited yet
            for k in range(l):
                i,j=q.popleft()
				# try all 4 directions from the current cell
                for l in range(4):
                    x=i+offsets[l][0]
                    y=j+offsets[l][1]
					# a invalid move
                    if(x<0 or y<0 or x>=rows or y>=cols or maze[x][y]=='+'):
                        continue
					# if we have reached the exit then current moves are the min moves to reach the exit
                    if(x==0 or y==0 or x==rows-1 or y==cols-1):
                        return moves
					# block the cell as we have visited
                    maze[x][y]='+'
                    q.append([x,y])
 
			# increment the moves
            moves+=1
            

        return -1