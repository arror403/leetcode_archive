class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return ({'a','e','i','o','u'} & set(s)) != set()