class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        L=len(score)
        if L==1: return ["Gold Medal"]
        elif L==2: return ["Gold Medal","Silver Medal"] if score[0]>score[1] else ["Silver Medal","Gold Medal"]
        

        t=sorted([[i,v] for i,v in enumerate(score)],key=lambda x:x[1],reverse=True)
        print(t)

        t[0][1]="Gold Medal"
        t[1][1]="Silver Medal"
        t[2][1]="Bronze Medal"


        for i in range(3,L): t[i][1]=str(i+1)

        return [x[1] for x in sorted(t,key=lambda x:x[0])]