class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        f=True
        m=[]
        s=s.split()
        for i in s:
            if i.isnumeric():
                m.append(i)
        # print(m)
        
        for i in range(1,len(m)):
            if int(m[i-1])<int(m[i]):
                continue
            else:
                f=False
                break
        return f
                