class ProductOfNumbers:

    def __init__(self):
        self.stream=[]

    def add(self, num: int) -> None:
        if num==0:
            self.stream=[]
        elif self.stream:
            self.stream.append(self.stream[-1]*num)
        else:
            self.stream.append(num)

    def getProduct(self, k: int) -> int:
        if k>len(self.stream):
            return 0
        if k==len(self.stream):
            return self.stream[-1]
        return self.stream[-1]//self.stream[-k-1]