class Solution:
    def groupThePeople(self, g: List[int]) -> List[List[int]]:
        g=[[i,v] for i,v in enumerate(g)]
        g=sorted(g, key = lambda x: x[1])
        result=[list(group) for key, group in groupby(g, key=lambda x: x[1])]
        res=[]

        for i in result:
            tmp = []
            group_size = i[0][1]
            for j in i:
                tmp.append(j[0])
                if len(tmp) == group_size:
                    res.append(tmp)
                    tmp = []        
        # for i in result:
        #     tmp=[]
        #     group_size=i[0][1]
        #     if len(i)>group_size:
        #         for j in i:
        #             if len(tmp)<group_size:
        #                 tmp.append(j[0])
        #             else:
        #                 res.append(tmp)
        #                 tmp=[]
        #     else:
        #         res.append([j[0] for j in i])

        return res