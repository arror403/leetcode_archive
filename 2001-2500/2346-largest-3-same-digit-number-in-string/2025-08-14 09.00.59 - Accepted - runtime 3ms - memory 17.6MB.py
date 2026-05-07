class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cur=None
        c=0
        max_good=-1

        for char in num:
            if char==cur:
                c+=1
                if c==3 and int(cur)>max_good:
                    max_good=int(cur)
            else:
                cur=char
                c=1
        

        return "" if max_good<0 else str(max_good)*3