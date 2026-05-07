class StockSpanner:

    def __init__(self):
        self.res=[]

    def next(self, price: int) -> int:
        r = 1
        while self.res and self.res[-1][0] <= price:
            r += self.res.pop()[1]
        self.res.append([price, r])
        return r

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)