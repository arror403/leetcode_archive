class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segment_count = 0
        prev_char = '0'  # Initialize the previous character as '0' to mark the start of a new segment
        
        for char in s:
            if char == '1' and prev_char == '0':
                segment_count += 1  # Increment the segment count when a new segment starts
            prev_char = char
        
        return segment_count <= 1