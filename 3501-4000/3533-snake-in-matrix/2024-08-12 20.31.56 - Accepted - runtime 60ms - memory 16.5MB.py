class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        d={"UP":[0,-1], "RIGHT":[1,0], "DOWN":[0,1], "LEFT":[-1,0]}
        i,j=0,0

        for s in commands:
            i+=d[s][0]
            j+=d[s][1]

        return (j*n)+i