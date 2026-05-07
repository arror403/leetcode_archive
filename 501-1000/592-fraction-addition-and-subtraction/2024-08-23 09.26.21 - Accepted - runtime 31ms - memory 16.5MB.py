from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        res=sum(map(Fraction, re.findall(r'[+-]?\d+/\d+', expression)))
        return f"{res.numerator}/{res.denominator}"