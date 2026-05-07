class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Create a graph where ingredients point to recipes they're used in
        graph = defaultdict(list)
        n = len(recipes)
        supplies_set = set(supplies)
        indegree = defaultdict(int)
        
        # Build the graph and calculate indegrees
        for i in range(n):
            for ingredient in ingredients[i]:
                if ingredient not in supplies_set:
                    # If an ingredient is not in supplies, add an edge from ingredient to recipe
                    graph[ingredient].append(recipes[i])
                    indegree[recipes[i]] += 1
        
        # Initialize queue with recipes that can be made immediately
        # (recipes with no missing ingredients or all ingredients in supplies)
        q = deque()
        for recipe in recipes:
            if indegree[recipe] == 0:
                q.append(recipe)
                
        res = []
        
        # KAHN'S ALGORITHM for topological sort
        while q:
            current_recipe = q.popleft()
            res.append(current_recipe)
            
            # Process all recipes that use this recipe as an ingredient
            for dependent_recipe in graph[current_recipe]:
                indegree[dependent_recipe] -= 1
                if indegree[dependent_recipe] == 0:
                    q.append(dependent_recipe)
        
        return res