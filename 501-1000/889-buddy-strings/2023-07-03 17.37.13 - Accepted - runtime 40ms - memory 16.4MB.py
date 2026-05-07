class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            # Check if s and goal are identical
            # In this case, we need at least one repeated character in s
            # to swap and make the strings equal
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False

        # Find the indices where the characters differ between s and goal
        diff_indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_indices.append(i)

        # Check if exactly two indices are different
        if len(diff_indices) != 2:
            return False

        # Swap the characters at the differing indices and check if the result matches goal
        i, j = diff_indices
        swapped = list(s)
        swapped[i], swapped[j] = swapped[j], swapped[i]
        swapped = ''.join(swapped)
        return swapped == goal