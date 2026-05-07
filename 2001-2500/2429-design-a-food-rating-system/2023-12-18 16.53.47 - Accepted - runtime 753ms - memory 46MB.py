
# Submitted by Samy Vilar <samy_vilar> on 10/30/2023

# For the sake of simplicity we will negate all ratings
# allowing us to use a min-heap, though while taking
# care to update any given negated rating updates;

# To determine our solution will apply a scan-line 
# approach in conjunction w/ a set of min-heaps
# each indexed by either a cuisione or any foods mapped 
# to their corresponding cuisine, should each min-heap
# store both the rated and food item, then our solution
# would be the root iff is "consistent", i.e. we will
# allow "stale" entries, taking care to evict said
# entries, each determined through a global/current
# ratings among all possible foods;

# For the sake of simplicity as well as performance, we will
# normalize all foods, by their correspoding rank,
# this way during heap-operations, at most 2 comparisons
# need be applied; otherwise each comparison would be
# contingent upon the length of any given food name;

# Given for any of q queries at worse we are traversing through some 
# heap at most log(q + |foods|) times it would imply O(q * (|foods| + log(q)))
# query time w/ some pre-processing time O(|foods| * k * |alphabet|)
# assuming any food entry has at most k symbols over some alphabet;

# version 1.1 micro-optimization(s)
#             - re-used paramters as auxillary storage
#             - used heapreplace instead of heappush, when ever possible;


# version 1.2 skipped normilization, while simplifying things,
#             it may or may not yield better timing(s)

class FoodRatings:
    def __init__(
        self, foods: List[str], cuisines: List[str], ratings: List[int],heapify=heapify, push=heappush, pop=heappop, replace=heapreplace,exhaust=deque(maxlen=0).extendleft):  
        roots = {}
        currently = {}
        heaps = defaultdict(list)
        for item, kind, rating in zip(foods, cuisines, ratings):            
            roots[kind] = roots[item] = (heap := heaps[kind])
            currently[item] = (rating := -rating)
            heap.append((rating, item))
        exhaust(map(heapify, heaps.values()))
        
        def changeRating(item, rating, currently=currently, roots=roots, push=push, replace=replace):            
            if currently[item] != (rating := -rating):
                currently[item] = rating
                got, other = (roots := roots[item])[0]
                (push if currently[other] == got else replace)(roots, (rating, item))
        self.changeRating = changeRating

        def highestRated(cuisine, roots=roots, currently=currently, pop=pop):
            roots = roots[cuisine]
            while True:
                rating, item = roots[0]
                if currently[item] == rating:
                    return item
                pop(roots)
        self.highestRated = highestRated
    


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)