class Solution:
    def maximumTime(self, time: str) -> str:
        t=list(time)
        # ['0','0',':','0','0']

        if t[0]=='?':
            if t[1] not in '?0123':
                t[0]='1'
            else:
                t[0]='2'
        if t[1]=='?':
            if t[0]=='0' or t[0]=='1':
                t[1]='9'
            else:
                t[1]='3'
        if t[3]=='?': t[3]='5'
        if t[4]=='?': t[4]='9'


        return ''.join(t)