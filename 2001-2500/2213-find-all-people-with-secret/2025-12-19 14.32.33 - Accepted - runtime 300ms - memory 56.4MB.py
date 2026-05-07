class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        res = {0,firstPerson}

        for _,g in groupby(sorted(meetings, key=lambda x:x[2]), key=lambda x:x[2]): 
            q = set()
            graph = defaultdict(list)
            for x,y,_ in g: 
                graph[x].append(y)
                graph[y].append(x)
                if x in res: q.add(x)
                if y in res: q.add(y)
                    
            q = deque(q)
            while q: 
                x = q.popleft()
                for y in graph[x]: 
                    if y not in res: 
                        res.add(y)
                        q.append(y)


        return list(res)