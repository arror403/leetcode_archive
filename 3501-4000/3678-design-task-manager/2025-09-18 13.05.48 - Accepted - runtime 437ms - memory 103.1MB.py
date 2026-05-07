class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.pq = []
        self.tasks = {}  # taskId -> (userId, priority) for O(1) lookups
        
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)
    
    def add(self, userId: int, taskId: int, priority: int) -> None:
        if taskId in self.tasks:
            self.rmv(taskId)
        
        self.tasks[taskId] = (userId, priority)
        # Heap entry: (-priority, -taskId) for max-heap behavior
        heapq.heappush(self.pq, (-priority, -taskId))
    
    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.tasks[taskId][0]
        self.add(userId, taskId, newPriority)
    
    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]
        # Note: Old entries remain in heap but will be filtered out during pop
    
    def execTop(self) -> int:
        while self.pq:
            neg_priority, neg_taskId = heapq.heappop(self.pq)
            taskId = -neg_taskId
            
            # Check if this task still exists and has matching priority
            if taskId in self.tasks and self.tasks[taskId][1] == -neg_priority:
                userId = self.tasks.pop(taskId)[0]
                return userId
        
        return -1