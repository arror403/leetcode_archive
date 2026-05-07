class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res=-inf
        for i in strs:
            for j in i:
                if j.isalpha():
                    if len(i)>res:
                        res=len(i)
                        break
            if i.isdigit():
                if int(i)>res:
                    res=int(i)

        return res