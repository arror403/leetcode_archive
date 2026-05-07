class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        while 1:
            r=[]
            for i in range(1, len(words)):
                if Counter(words[i-1])==Counter(words[i]):
                    r.append(i)

            if r==[]: break

            for j in reversed(r): del words[j]


        return words