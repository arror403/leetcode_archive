class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res=0
        d=set()

        for x in permutations(digits, 3):
            tmp=x[0]*100+x[1]*10+x[2]
            if tmp%2==0 and 100<=tmp<=999:
                if tmp not in d:
                    d.add(tmp)
                    res+=1


        return res