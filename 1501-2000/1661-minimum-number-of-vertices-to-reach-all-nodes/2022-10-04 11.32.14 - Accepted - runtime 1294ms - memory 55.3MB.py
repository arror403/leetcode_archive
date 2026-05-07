class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Function to find smallest set
        # of vertices from which the
        # complete graph can be visited
        def solver(edges):
    
            graph = defaultdict(list)
    
            # dictionary storing
            # indegree of nodes
            indeg = defaultdict(int)
    
            for (u,v) in edges:
                graph[u].append(v)
    
                # count indegree of
                # each node
                indeg[v] +=1
    
            ans = []
            for u in graph:
                
                # add to ans, if indegree
                # of node u is 0
                if(indeg[u] == 0):
                    ans.append(u)
    
            # Return Ans
            return (ans)
        return solver(edges)