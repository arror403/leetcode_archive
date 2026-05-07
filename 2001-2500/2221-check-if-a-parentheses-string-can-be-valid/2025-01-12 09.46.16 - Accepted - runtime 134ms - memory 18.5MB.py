class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        def validate(op):
            bal=wild=0
            sz=len(s)

            start=0 if op=="(" else sz-1
            d=1 if op=='(' else -1

            i=start
            while(i>=0 and i<sz and wild+bal>=0):
                if locked[i]=="1":
                    bal+=1 if s[i]==op else -1
                else:
                    wild+=1
                i+=d

            return abs(bal)<=wild


        return len(s)%2==0 and validate('(') and validate(')')