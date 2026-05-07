class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def topological_sort(conditions, k):
            graph=defaultdict(list)
            in_degree=[0]*(k+1)
            
            for u,v in conditions:
                graph[u].append(v)
                in_degree[v]+=1
            
            q=deque([i for i in range(1,k+1) if in_degree[i]==0])
            sorted_order=[]
            
            while q:
                node=q.popleft()
                sorted_order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor]-=1
                    if in_degree[neighbor]==0: q.append(neighbor)
            

            return sorted_order if len(sorted_order)==k else []
        

        row_order=topological_sort(rowConditions, k)
        col_order=topological_sort(colConditions, k)
        
        if not row_order or not col_order: return []
        
        row_pos={v:i for i,v in enumerate(row_order)}
        col_pos={v:i for i,v in enumerate(col_order)}
        
        matrix = [[0]*k for _ in range(k)]

        for v in range(1,k+1): matrix[row_pos[v]][col_pos[v]]=v
        

        return matrix