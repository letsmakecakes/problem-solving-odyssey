class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals.

        Args:
            intervals: List of intervals where each interval is [start, end]

        Returns:
            List of merged intervals with no overlaps
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(n) for the result array
        """
        # Handle edge cases
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort(key=lambda interval: interval[0])

        merged = [intervals[0]] # Start with first interval

        for current in intervals[1:]:
            last_merged = merged[-1]

            # Check if current interval overlaps with the last merged interval
            if self._intervals_overlap(last_merged, current):
                # Merge by extending the end time
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add current interval as new
                merged.append(current)

        return merged
    
    def _intervals_overlap(self, interval1: List[int], interval2: List[int]) -> bool:
        """
        Check if two intervals overlap.

        Args:
            interval1: First interval [start, end]
            interval2: Second interval [start, end]
        
        Returns:
            True if intervals overlap or are adjacent, False otherwise
        """
        return interval1[1] >= interval2[0]