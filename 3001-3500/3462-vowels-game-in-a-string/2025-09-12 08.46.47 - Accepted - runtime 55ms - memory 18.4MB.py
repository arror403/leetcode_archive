class Solution:
    def doesAliceWin(self, s: str) -> bool:
        d=Counter(s)

        return (d['a']+d['e']+d['i']+d['o']+d['u'])!=0

        # return sum(c in "aeiou" for c in s)!=0

        # return ({'a','e','i','o','u'} & set(s)) != {}