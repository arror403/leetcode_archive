class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        missing=len(t) # total chars we need
        begin=end=head=0
        d=inf
        
        while end<len(s):
            if need[s[end]]>0: missing-=1
            need[s[end]]-=1
            end+=1
            
            while missing==0:
                if (end-begin)<d:
                    head=begin
                    d=end-begin
                if need[s[begin]]==0: missing+=1
                need[s[begin]]+=1
                begin+=1


        return "" if d==inf else s[head:head+d]