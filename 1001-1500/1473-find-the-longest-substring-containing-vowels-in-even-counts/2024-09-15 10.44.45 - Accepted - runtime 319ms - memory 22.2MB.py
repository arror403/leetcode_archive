class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels={'a':0,'e':1,'i':2,'o':3,'u':4}
        state={0:-1}
        cur_state=max_length=0

        for i,c in enumerate(s):
            if c in vowels:
                cur_state ^= 1<<vowels[c]
            if cur_state in state:
                max_length = max(max_length, i-state[cur_state])
            else:
                state[cur_state] = i


        return max_length