class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        n = len(recipes)
        supplies_set = set(supplies)
        indegree = defaultdict(int)

        for i in range(n):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] not in supplies_set:
                    graph[ingredients[i][j]].append(recipes[i])  # if the ingredient required to make a recipe is not in supplies then  
                    indegree[recipes[i]]+=1 #we need to make a directed edge from that ingredient to recipe

        # KAHN'S ALGORITHM
        q = deque()
        for recipe in recipes:
            if indegree[recipe] == 0:
                q.append(recipe)
                
        res = []

        while q:
            tmp=q.popleft()
            res.append(tmp)
            for nbr in graph[tmp]:
                indegree[nbr]-=1
                if indegree[nbr]==0:
                    q.append(nbr)

        return res