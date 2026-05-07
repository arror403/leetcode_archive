class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d=Counter(tasks).values()
        max_freq=max(d)
        max_count=len([i for i in d if i==max_freq])
        # max_count=d.count(max_freq)

        return max(len(tasks), (max_freq-1)*(n+1)+max_count)