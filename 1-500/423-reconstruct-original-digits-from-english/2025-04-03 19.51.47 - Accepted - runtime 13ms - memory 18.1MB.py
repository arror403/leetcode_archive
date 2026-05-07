class Solution:
    def originalDigits(self, s: str) -> str:
        d=Counter(s)
        res=""
        # zero one two three four five six seven eight nine
        # zero one two thre  four five six sevn  eight nie
        # z        w         u         x         g
        #      o       t          f

        res+='0'*d['z']
        d['e']-=d['z']
        d['r']-=d['z']
        d['o']-=d['z']

        res+='2'*d['w']
        d['t']-=d['w']
        d['o']-=d['w']

        res+='4'*d['u']
        d['f']-=d['u']
        d['o']-=d['u']
        d['r']-=d['u']

        res+='6'*d['x']
        d['s']-=d['x']
        d['i']-=d['x']

        res+='8'*d['g']
        d['e']-=d['g']
        d['i']-=d['g']
        d['h']-=d['g']
        d['t']-=d['g']

        res+='5'*d['f']
        d['i']-=d['f']
        d['v']-=d['f']
        d['e']-=d['f']

        res+='3'*d['t']
        d['h']-=d['t']
        d['r']-=d['t']
        d['e']-=d['t']*2

        res+='1'*d['o']
        d['n']-=d['o']
        d['e']-=d['o']

        res+='7'*d['v']
        d['s']-=d['v']
        d['e']-=d['v']*2
        d['n']-=d['v']

        res+='9'*d['i']


        return ''.join(sorted(res))