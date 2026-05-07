    # def back(self, steps: int) -> str:
    #     self.x = max(0, self.x - steps)
    #     return self.h[self.x]

    # def forward(self, steps: int) -> str:
    #     self.x = min(len(self.h) - 1, self.x + steps)
    #     return self.h[self.x]

class BrowserHistory:

    def __init__(self, homepage: str):
        self.h=[homepage]
        self.x=0

    # def visit(self, url: str) -> None:
    #     if url not in self.h:
    #         self.x+=1
    #         self.h.append(url)
    #     else:
    #         for i,v in enumerate(self.h):
    #             if v==url:
    #                 self.x=i
    #                 self.h=self.h[:i+1]

    def visit(self, url: str) -> None:
        self.x+=1
        self.h=self.h[:self.x]
        self.h.append(url)

    def back(self, steps: int) -> str:
        if (t:=self.x-steps)>=0:
            self.x=t
            return self.h[t]
        else:
            self.x=0
            return self.h[0]

    def forward(self, steps: int) -> str:
        if (t:=self.x+steps)<len(self.h):
            self.x=t
            return self.h[t]
        else:
            self.x=len(self.h)-1
            return self.h[-1]