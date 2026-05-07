class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power_value(x):
            p=0
            while x!=1:
                if x%2: x=(x*3)+1
                else: x//=2
                p+=1
            
            return p


        d={i:power_value(i) for i in range(lo, hi+1)}

        sorted_dict=dict(sorted(d.items(), key=lambda x: (x[1], x[0])))
        # print(sorted_dict)


        return list(sorted_dict.keys())[k-1]