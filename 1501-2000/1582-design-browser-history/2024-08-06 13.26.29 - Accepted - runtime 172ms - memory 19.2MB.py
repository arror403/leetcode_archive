class BrowserHistory:

    def __init__(self, homepage: str):
        self.h=[homepage]
        self.x=0

    def visit(self, url: str) -> None:
        self.x+=1
        self.h=self.h[:self.x]
        self.h.append(url)

    def back(self, steps: int) -> str:
        self.x=max(0, self.x-steps)
        return self.h[self.x]

    def forward(self, steps: int) -> str:
        self.x=min(len(self.h)-1, self.x+steps)
        return self.h[self.x]