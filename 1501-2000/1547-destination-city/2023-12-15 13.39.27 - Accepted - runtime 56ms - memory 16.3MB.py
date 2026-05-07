class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Use a set to store starting cities
        start_cities = set()

        # Add all starting cities to the set
        for path in paths:
            start_cities.add(path[0])

        # Find the destination city
        for path in paths:
            if path[1] not in start_cities:
                return path[1]