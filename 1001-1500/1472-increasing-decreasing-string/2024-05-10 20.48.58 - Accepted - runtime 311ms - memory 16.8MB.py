class Solution:
    def sortString(self, s: str) -> str:
        res=[]
        d=deque(sorted(s))

        while d:
            res+=d.popleft()
            while 1:
                f=1
                for i in d:
                    if i>res[-1]:
                        f=0
                        res.append(i)
                        d.remove(i)
                        break
                if f: break

            if not d: return ''.join(res)

            res+=d.pop()
            while 1:
                f=1
                for i in reversed(d):
                    if i<res[-1]:
                        f=0
                        res.append(i)
                        d.remove(i)
                        break
                if f: break


        return ''.join(res)