class Solution:
    def largestIsland(self, g: List[List[int]]) -> int:
        rows, cols = len(g), len(g[0])
        
        # First find the biggest current island
        def paint(i, j, c):
            if i < 0 or i >= rows or j < 0 or j >= cols or g[i][j] != 1:
                return 0
            g[i][j] = c
            return 1 + paint(i+1, j, c) + paint(i-1, j, c) + \
                   paint(i, j+1, c) + paint(i, j-1, c)
        
        # Color each island and store its size
        color = 2  # Start coloring from 2
        color_sizes = {}  # Maps color -> size of island
        for i in range(rows):
            for j in range(cols):
                if g[i][j] == 1:
                    size = paint(i, j, color)
                    color_sizes[color] = size
                    color += 1
        
        # If no islands exist
        if not color_sizes:
            return 1
            
        # If no 0s exist (all 1s)
        if len(color_sizes) == 1 and list(color_sizes.values())[0] == rows * cols:
            return rows * cols
            
        # Try to connect islands by changing one 0 to 1
        max_size = max(color_sizes.values()) if color_sizes else 0
        
        for i in range(rows):
            for j in range(cols):
                if g[i][j] == 0:
                    # Get unique colors of neighbors
                    neighbor_colors = set()
                    for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                        if 0 <= ni < rows and 0 <= nj < cols and g[ni][nj] > 1:
                            neighbor_colors.add(g[ni][nj])
                    
                    # Calculate total size if we change this 0 to 1
                    total_size = 1  # Count the cell we're changing
                    for color in neighbor_colors:
                        total_size += color_sizes[color]
                    max_size = max(max_size, total_size)
        
        return max_size

# class Solution:
#     def largestIsland(self, g: List[List[int]]) -> int:
#         res=0
#         # g=tuple(tuple(l) for l in grid)

#         @lru_cache(maxsize=None)
#         def paint(i, j, c, g, flip=False):
#             if (not flip and (min(i,j)<0 or i>=len(g) or j>=len(g[0]) or g[i][j]==0 or g[i][j]==c)):
#                 return 0

#             g[i][j]=0 if g[i][j]==0 else c

#             return 1+paint(i+1, j, c, g)+paint(i-1, j, c, g)+paint(i, j+1, c, g)+paint(i, j-1, c, g)

    
#         for i in range(len(g)):
#             for j in range(len(g[i])):
#                 if g[i][j]==0:
#                     res=max(res, paint(i, j, 2, g, True))
#                     paint(i, j, 1, g, True)


#         return len(g)*len(g[0]) if res==0 else res