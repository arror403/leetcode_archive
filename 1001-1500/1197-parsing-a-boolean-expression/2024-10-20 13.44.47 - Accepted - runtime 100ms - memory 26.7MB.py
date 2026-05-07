class Solution:
    def parseBoolExpr(self, S: str, t=True, f=False) -> bool:
        return eval(S.replace('!','not |').replace('&(','all([').replace('|(','any([').replace(')','])'))