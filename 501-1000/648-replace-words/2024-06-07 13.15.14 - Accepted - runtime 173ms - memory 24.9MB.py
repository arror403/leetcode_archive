class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence=sentence.split()
        dictionary.sort(key=len)
        res=[]

        for w in sentence:
            F=1
            for d in dictionary:
                if w.startswith(d):
                    res.append(d)
                    F=0
                    break
            if F: res.append(w)


        return ' '.join(res)