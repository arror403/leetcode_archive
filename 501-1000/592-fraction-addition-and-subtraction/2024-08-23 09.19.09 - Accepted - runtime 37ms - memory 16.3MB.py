from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions=re.findall(r'[+-]?\d+/\d+', expression)
        res=str(sum(Fraction(i) for i in fractions))

        
        return res if '/' in res else res+'/1'