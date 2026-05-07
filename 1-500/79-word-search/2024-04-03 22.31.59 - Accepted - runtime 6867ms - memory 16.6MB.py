class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        m=defaultdict(list)
        # Creating a mapping of characters to their indexes in the grid
        for i,row in enumerate(board):
            for j,c in enumerate(row):
                m[c].append((i,j))

        visited=set()

        def dfs(i, j, idx):
            if idx==len(word): return True
            
            if i<0 or i>=rows or j<0 or j>=cols or (i,j) in visited or board[i][j]!=word[idx]:
                return False
            
            visited.add((i,j))

            # Check adjacent cells
            if any(dfs(x,y,idx+1) for x,y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]):
                return True

            visited.remove((i,j))
            return False

        # Iterate through each starting position of the word
        for start_pos in m[word[0]]:
            if dfs(start_pos[0], start_pos[1], 0):
                return True

        return False



        # m=defaultdict(list)

        # for i,r in enumerate(board):
        #     for j,c in enumerate(r):
        #         m[c].append([i,j])

        # p=[]

        # for w in word:
        #     if w not in m.keys(): return 0
        #     else: p.append(m[w])

        # # print(p)

        # return self.are_adjacent(p)


    # def get_neighbors(self, a, rows, cols):
    #     t=[]
    #     if (a[1]+1)<cols:
    #         t.append([a[0], a[1]+1])
    #     if a[1]>0:
    #         t.append([a[0], a[1]-1])
    #     if a[0]>0:
    #         t.append([a[0]-1, a[1]])
    #     if (a[0]+1)<rows:
    #         t.append([a[0]+1, a[1]])
    #     return t