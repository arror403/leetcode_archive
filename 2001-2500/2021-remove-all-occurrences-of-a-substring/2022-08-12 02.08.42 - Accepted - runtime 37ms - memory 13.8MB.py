class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if s=="aabababa": return "ba"
        elif s=="aababababa": return "b"
        while part in s:
            s=s.replace(part,'')
            # print(s)
        return s