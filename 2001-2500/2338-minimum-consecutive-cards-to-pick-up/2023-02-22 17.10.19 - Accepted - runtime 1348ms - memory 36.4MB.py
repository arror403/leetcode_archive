class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(dict.fromkeys(cards))==len(cards): return -1
        res=inf
        t=[]
        for i in range(len(cards)):
            tmp=[cards[i],i]
            t.append(tmp)

        t=sorted(t, key=lambda x:x[0])

        for i in range(len(t)-1):
            if (t[i][0]==t[i+1][0]):
                tmp=abs(t[i][1]-t[i+1][1])+1
                if tmp<res: res=tmp
        # print(t)

        return res