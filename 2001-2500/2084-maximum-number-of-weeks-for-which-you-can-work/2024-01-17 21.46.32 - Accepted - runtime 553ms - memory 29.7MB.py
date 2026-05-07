class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:

        ##### power by chatGPT #####

        max_freq = max(milestones)
        total_freq = sum(milestones)
        remaining_freq = total_freq - max_freq

        if max_freq <= remaining_freq + 1:
            return total_freq
        else:
            return 2 * remaining_freq + 1