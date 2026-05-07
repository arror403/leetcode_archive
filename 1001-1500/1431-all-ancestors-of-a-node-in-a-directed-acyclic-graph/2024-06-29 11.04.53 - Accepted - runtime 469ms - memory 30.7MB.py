class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        in_degree=[0]*n
        paths = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            in_degree[b]+=1

        queue=[x for x in range(n) if in_degree[x]==0]

        while queue:
            node=queue.pop(0)
            # Update paths of children
            for child in graph[node]:
                if not paths[child]:
                    paths[child]=list(dict.fromkeys(paths[node] + [node]))
                else:
                    paths[child]=list(dict.fromkeys(paths[child] + paths[node] + [node]))
                
                in_degree[child]-=1
                
                if in_degree[child]==0:
                    queue.append(child)


        return map(sorted, paths)