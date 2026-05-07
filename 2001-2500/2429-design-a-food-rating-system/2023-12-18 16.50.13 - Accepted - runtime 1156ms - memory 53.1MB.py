from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        # Initialize two dictionaries to store our food ratings and sorted sets
        # Maps each food to its cuisine and rating
        self.food_to_cuisine_and_rating = {}
        # Maps each cuisine to a sorted set of tuples with ratings and corresponding food names
        self.cuisine_to_sorted_foods = defaultdict(lambda: SortedSet(key=lambda x: (-x[0], x[1])))
        # Populate the dictionaries with the initial list of foods, cuisines, and ratings
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine_and_rating[food] = (cuisine, rating)
            self.cuisine_to_sorted_foods[cuisine].add((rating, food))


    def changeRating(self, food, new_rating):
        """
        Update the rating of the specified food.
        """
        # Retrieve the current cuisine and rating for the food
        cuisine, current_rating = self.food_to_cuisine_and_rating[food]
        # Update the food's rating in the mapping
        self.food_to_cuisine_and_rating[food] = (cuisine, new_rating)
        # Remove the old rating from the sorted set and add the new rating
        self.cuisine_to_sorted_foods[cuisine].remove((current_rating, food))
        self.cuisine_to_sorted_foods[cuisine].add((new_rating, food))


    def highestRated(self, cuisine):
        """
        Return the name of the food that has the highest rating for the given cuisine.
        """
        # The first element of the SortedSet for the cuisine has the highest rating due to sorting order
        return self.cuisine_to_sorted_foods[cuisine][0][1]
      

# Note: While the method names are not modified as per instructions (changeRating, highestRated), 
# the variable naming has been standardized to adhere to Python's snake_case convention.