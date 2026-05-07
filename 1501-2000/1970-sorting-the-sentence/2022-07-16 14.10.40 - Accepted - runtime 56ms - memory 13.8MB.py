class Solution:
    def sortSentence(self, s: str) -> str:
        w=[]
        res=[]
        s=s.split()
        for i in s:
            tmp=[]
            tmp.append(int(i[-1]))
            tmp.append(i.replace(i[-1],''))
            w.append(tmp)

        w.sort(key=lambda row:(row[0]), reverse=False)
        for i in w: res.append(i[1])
        res=' '.join(res)

        # print(w)
        return (res)