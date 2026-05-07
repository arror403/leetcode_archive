class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove_pairs(s: str, first: str, second: str, score: int) -> tuple[str, int]:
            stack=[]
            total_score=0
            for c in s:
                if stack and (stack[-1],c)==(first,second):
                    stack.pop()
                    total_score+=score
                else:
                    stack.append(c)
            
            return ''.join(stack), total_score

        if x>y:
            first,second=('a','b')
            first_score,second_score=(x,y)
        else:
            first,second=('b','a')
            first_score,second_score=(y,x)

        s,score1 = remove_pairs(s, first, second, first_score)
        _,score2 = remove_pairs(s, second, first, second_score)


        return score1+score2



        # d=defaultdict(list)
        # for i,c in enumerate(s):
        #     if c=='a': d['a'].append(i)
        #     elif c=='b': d['b'].append(i)
        # print(d)

        # return 0



        # if (L:=len(s))==1: return 0
        # t=[]
        # res=0
        # ca,ca=1,1
        # m=['a','b']
        # f=x>y

        # if (s[0] in m and s[1] in m): t.append(s[0])
        # for i in range(1,L-1):
        #     if s[i] in m:
        #         if (s[i-1] in m) or (s[i+1] in m):
        #             t.append(s[i])

        # if (s[-1] in m and s[-2] in m): t.append(s[-1])

        # while t and (ca or cb):
        #     if f:
        #         ca=False
        #         for i in range(len(t)-1):
        #             if (t[i]+t[i+1])=="ab":
        #                 ca=True
        #                 del t[i]
        #                 del t[i]
        #                 res+=x
        #                 break
        #         f = not f
        #     else:
        #         cb=False
        #         for i in range(len(t)-1):
        #             if (t[i]+t[i+1])=="ba":
        #                 cb=True
        #                 del t[i]
        #                 del t[i]
        #                 res+=y
        #                 break
        #         f = not f


        # return res