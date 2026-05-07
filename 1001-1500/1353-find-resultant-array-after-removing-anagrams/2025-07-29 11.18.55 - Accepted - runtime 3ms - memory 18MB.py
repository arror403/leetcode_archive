class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        m=[sorted(w) for w in words]

        while 1:
            r=[]
            for i in range(1, len(words)):
                if m[i-1]==m[i]:
                    r.append(i)

            if r==[]: break

            for j in r[::-1]: 
                del words[j]
                del m[j]


        return words