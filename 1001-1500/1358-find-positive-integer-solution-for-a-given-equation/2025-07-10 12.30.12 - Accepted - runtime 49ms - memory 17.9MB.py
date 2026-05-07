class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res=[]
        y=1000

        for x in range(1, 1001):
            while y > 1 and customfunction.f(x, y) > z:
                y -= 1
            if customfunction.f(x, y) == z:
                res.append([x, y])

    
        return res



        # 1: a + b
        # 2: a * b
        # 3: a**2 + b
        # 4: a + b**2
        # 5: a**2 + b**2
        # 6: (a+b)**2
        # 7: a**3 + b**3
        # 8: a**2 * b
        # 9: a * b**2

        # def f1(): return [[i,z-i] for i in range(1, 1001) if z>i]

        # def f2(): return [[z//i,i] for i in range(1, 1001) if z%i==0]

        # def f3(): return [[i,z-i**2] for i in range(1, 1001) if z>i**2]

        # def f4(): return [[z-i**2,i] for i in range(1, 1001) if z>i**2]

        # def f5(): return [[i,sqrt(z-i**2)] for i in range(1, 1001) if sqrt(z-i**2)==int(sqrt(z-i**2))]

        # def f6(): return [[i,sqrt(z)-i] for i in range(1, 1001) if sqrt(z)==int(sqrt(z))]

        # def f7():
        
        # def f8():

        # def f9():
        
        # l={10:f1, 21:f2, 16:f3, 52:f4, 58:f5, 100:f6, 370:f7, 63:f8, 147:f9}


        # obj=CustomFunction(4)
        # function_id=obj.f(3, 7)


        # return l[function_id]()