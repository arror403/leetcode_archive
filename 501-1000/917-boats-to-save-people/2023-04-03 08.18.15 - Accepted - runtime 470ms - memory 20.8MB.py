class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort people in ascending order
        people.sort()
        
        # Use two pointers to group together the lightest and heaviest people
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            # If the heaviest person can fit in the boat with the lightest person, increment left
            if people[right] + people[left] <= limit:
                left += 1
            right -= 1
            boats += 1
        
        return boats