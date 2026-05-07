class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for i in range(1,len(words)+1):
            tmp=words[:i]
            # print (tmp)
            tmp=''.join(tmp)
            if tmp==s: return True

        return False