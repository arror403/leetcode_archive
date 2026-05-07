class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        L=k%len(s)
        s=deque(s)
        s.rotate(-L)
        return ''.join(s)