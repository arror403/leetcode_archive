class Solution:
    def canMakeSquare(self, m: List[List[str]]) -> bool:
        m1=m[0][0]+m[0][1]+m[1][0]+m[1][1]
        m2=m[0][1]+m[0][2]+m[1][1]+m[1][2]
        m3=m[1][0]+m[1][1]+m[2][0]+m[2][1]
        m4=m[1][1]+m[1][2]+m[2][1]+m[2][2]

        for t in map(lambda x: ''.join(sorted(x)), [m1,m2,m3,m4]):
            if t in ["BBBW","BWWW","BBBB","WWWW"]:
                return True

        return False