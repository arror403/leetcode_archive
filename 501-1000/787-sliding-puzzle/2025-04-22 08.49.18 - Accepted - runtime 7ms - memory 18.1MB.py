class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def swap(s, i, j):
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            return "".join(s_list)

        target = "123450"
        start = ""

        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        
        visited = set()
        # All positions where 0 can be swapped to from each position
        # For a 2x3 board, these are the adjacent positions for each cell
        dirs = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        
        queue = deque([start])
        visited.add(start)
        res = 0
        
        while queue:
            # Level count for BFS
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur == target:
                    return res
                
                zero = cur.index('0')
                # Try all possible swaps
                for dir in dirs[zero]:
                    next_state = swap(cur, zero, dir)
                    if next_state in visited:
                        continue
                    visited.add(next_state)
                    queue.append(next_state)
            
            res += 1
        

        return -1