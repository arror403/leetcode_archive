class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1: return word

        n=len(word)
        m=n-numFriends+1

        return max(word[i:i+m] for i in range(n))