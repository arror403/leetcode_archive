class Solution:
    def countTime(self, time: str) -> int:
        res = 1
        
        if time[4] == '?': res *= 10
        if time[3] == '?': res *= 6
        
        if time[0]+time[1] == '??':
            res *= 24
        else:
            if time[1] == '?':
                if time[0] == '2':
                    res *= 4
                else:
                    res *= 10
            if time[0] == '?':
                if int(time[1]) < 4: 
                    res *= 3
                else:
                    res *= 2


        return res


        # t=list(time)
        # l=['0' if x=='?' else x for x in t]
            

        # if t[0]=='?':
        #     if t[1] not in '?0123':
        #         t[0]='1'
        #     else:
        #         t[0]='2'
        # if t[1]=='?':
        #     if t[0]=='0' or t[0]=='1':
        #         t[1]='9'
        #     else:
        #         t[1]='3'
        # if t[3]=='?': t[3]='5'
        # if t[4]=='?': t[4]='9'


        # return (int(t[0]+t[1])-int(l[0]+l[1])+1)*(int(t[3]+t[4])-int(l[3]+l[4])+1)