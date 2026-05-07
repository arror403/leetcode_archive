class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        if not board: return
        
        # Pre-compute sets for faster validation
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        
        # Initialize sets with existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.boxes[3*(i//3) + j//3].add(num)
        
        self.solve(board)
    
    def solve(self, board):
        # Find empty cell with minimum remaining values (MRV heuristic)
        min_choices = 10
        best_cell = None
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    choices = 0
                    for c in "123456789":
                        if self.isValid(i, j, c):
                            choices += 1
                    
                    if choices < min_choices:
                        min_choices = choices
                        best_cell = (i, j)
                        if choices == 0:  # No valid choices, early fail
                            return False
        
        if best_cell is None:  # No empty cells left
            return True
            
        i, j = best_cell
        for c in "123456789":
            if self.isValid(i, j, c):
                board[i][j] = c
                
                # Update sets
                box_idx = 3*(i//3) + j//3
                self.rows[i].add(c)
                self.cols[j].add(c)
                self.boxes[box_idx].add(c)
                
                if self.solve(board):
                    return True
                
                # Backtrack
                board[i][j] = '.'
                self.rows[i].remove(c)
                self.cols[j].remove(c)
                self.boxes[box_idx].remove(c)
        
        return False
    
    def isValid(self, row, col, c):
        box_idx = 3*(row//3) + col//3
        return (c not in self.rows[row] and 
                c not in self.cols[col] and 
                c not in self.boxes[box_idx])