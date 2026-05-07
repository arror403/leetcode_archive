class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.p=PrioritizedItem()
        for u, t, p in tasks: self.p.add_task(u, t, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.p.add_task(userId, taskId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.p.entry_finder[taskId][3]
        self.p.add_task(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        self.p.remove_task(taskId)

    def execTop(self) -> int:
        return self.p.pop_task()



class PrioritizedItem:

    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = itertools.count()

    def add_task(self, user, task, priority):
        if task in self.entry_finder: self.remove_task(task)
        count = next(self.counter)
        entry = [-priority, -task, count, user, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[4] = '<removed-task>'

    def pop_task(self):
        while self.pq:
            t = heappop(self.pq)
            if t[4] != '<removed-task>':
                del self.entry_finder[t[4]]
                return t[3]
        return -1