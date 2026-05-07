class MyQueue:

    ##### power by chatGPT #####

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def push(self, x: int) -> None:
        self.stack_push.append(x)

    def pop(self) -> int:
        self.move_elements()
        return self.stack_pop.pop()

    def peek(self) -> int:
        self.move_elements()
        return self.stack_pop[-1]

    def empty(self) -> bool:
        return not self.stack_push and not self.stack_pop

    def move_elements(self) -> None:
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
