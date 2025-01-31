class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Handle edge cases
        if not intervals or len(intervals) <= 1:
            return intervals
        
        # Sort intervals based on start time to enable linear merging
        intervals.sort(key=lambda x: x[0])

        # Initialize merged intervals list
        merged = []

        for interval in intervals:
            # If merged list is empty or no overlap, add current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge overlapping intervals by extending the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged