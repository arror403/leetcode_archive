class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        m=[]

        for addr in emails:
            tmp=''
            i=addr.index('@')

            for c in addr[:i]:
                if c=='.': continue
                elif c=='+': break
                else: tmp+=c

            m.append(tmp+addr[i:])
        # print(m)

        return len(list(set(m)))