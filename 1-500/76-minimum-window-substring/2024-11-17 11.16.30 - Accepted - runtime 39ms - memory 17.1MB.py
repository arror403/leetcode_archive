class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp=[0]*128
        for c in t: mp[ord(c)]+=1
        count=len(t)
        begin=end=head=0
        d=inf

        while end<len(s):
            if mp[ord(s[end])]>0: count-=1
            mp[ord(s[end])]-=1
            end+=1
            while count==0:
                if(end-begin)<d:
                    head=begin
                    d=end-head
                if mp[ord(s[begin])]==0: count+=1
                mp[ord(s[begin])]+=1
                begin+=1
                

        return "" if d==inf else s[head:head+d]