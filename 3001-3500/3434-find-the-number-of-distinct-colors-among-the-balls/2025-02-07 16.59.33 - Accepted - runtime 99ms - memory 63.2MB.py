class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        ball_map = {}  
        color_freq = Counter()  

        for ball, color in queries:
            if ball in ball_map:
                old_color = ball_map[ball]
                color_freq[old_color] -= 1
                if color_freq[old_color] == 0:
                    del color_freq[old_color]  

            ball_map[ball] = color
            color_freq[color] += 1

            res.append(len(color_freq))


        return res



        # m=[-1]*(limit+1)
        # s=set()
        # L=0
        # res=[]

        # for i,c in queries:
        #     m[i]=c
        #     if c not in s: 
        #         s.add(c)
        #         L+=1
        #     res.append(L)


        # return res