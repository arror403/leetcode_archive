class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a=ord(coordinates[0])-97
        b=int(coordinates[1])-1
        map=[[0,1,0,1,0,1,0,1],
             [1,0,1,0,1,0,1,0],
             [0,1,0,1,0,1,0,1],
             [1,0,1,0,1,0,1,0],
             [0,1,0,1,0,1,0,1],
             [1,0,1,0,1,0,1,0],
             [0,1,0,1,0,1,0,1],
             [1,0,1,0,1,0,1,0]]
        
        return map[a][b]
                