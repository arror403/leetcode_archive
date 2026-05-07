class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [map(lambda x: ~x&1,reversed(i)) for i in image]