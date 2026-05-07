class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        flag=0
        if num==6:flag=1
        elif num==28:flag=1
        elif num==496:flag=1
        elif num==8128:flag=1
        elif num==33550336:flag=1
            
        return flag