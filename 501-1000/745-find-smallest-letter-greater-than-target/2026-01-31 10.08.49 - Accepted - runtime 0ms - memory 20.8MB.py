class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        L=len(letters)-1
        l, r = 0, L

        if target >= letters[L] or target < letters[0]:
            return letters[0]

        while l <= r:
            mid = l+(r-l)//2

            if letters[mid] <= target:
                l=mid+1
            else:
                r=mid-1


        return letters[l]