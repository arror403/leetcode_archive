class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        if s1 == s2:
            return True
        
        # Find the positions where s1 and s2 differ
        diff_positions = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_positions.append(i)
        
        # If there are more than two positions that differ, we can't make the strings equal
        if len(diff_positions) != 2:
            return False
        
        # Check if swapping the characters at the different positions results in equal strings
        i, j = diff_positions
        # print (i,j)
        # print(diff_positions)
        return s1[i] == s2[j] and s1[j] == s2[i]