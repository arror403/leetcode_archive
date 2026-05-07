class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        a,b,c=set(),set(),set()

        for i,v in enumerate(code):
            v=v.replace('_','a')
            if v.isalnum():
                a.add(i)

        for i,v in enumerate(businessLine):
            if v in ["electronics", "grocery", "pharmacy", "restaurant"]:
                b.add(i)

        for i,v in enumerate(isActive):
            if v:
                c.add(i)

        res=[[code[i], businessLine[i], isActive[i]] for i in a&b&c]
        
        res.sort(key=lambda x:(x[1], x[0]))


        return [x[0] for x in res]