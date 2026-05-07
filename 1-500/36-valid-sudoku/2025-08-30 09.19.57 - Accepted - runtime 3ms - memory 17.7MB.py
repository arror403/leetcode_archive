class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            t=set()
            for x in r:
                if x.isnumeric():
                    if x in t: return False
                    else: t.add(x)

        for c in zip(*board):
            t=set()
            for x in c:
                if x.isnumeric():
                    if x in t: return False
                    else: t.add(x)

        m33=[]
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                t=[]
                for x in board[i:i+3]:
                    t+=x[j:j+3]
                # t=[x[j:j+3] for x in board[i:i+3]]
                # print(t)
                m33.append(t)
        # print(m33)

        for k in m33:
            t=set()
            for x in k:
                if x.isnumeric():
                    if x in t: return False
                    else: t.add(x)


        return True