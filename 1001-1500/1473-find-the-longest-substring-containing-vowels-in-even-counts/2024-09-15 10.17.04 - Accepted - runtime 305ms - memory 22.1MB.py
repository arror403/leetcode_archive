class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels='aeiou'
        state={0:-1}
        cur_state=max_length=0

        for i,c in enumerate(s):
            if c in vowels:
                cur_state ^= 1<<vowels.index(c)
            if cur_state in state:
                max_length = max(max_length, i-state[cur_state])
            else:
                state[cur_state] = i


        return max_length