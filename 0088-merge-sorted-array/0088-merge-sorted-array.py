class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place in sorted order.
        Uses three-pointer approach starting from the end for O(m+n) time complexity.
        """
        # Start from the end of both arrays
        i = m - 1     # Last element in the valid portion of nums1
        j = n - 1     # Last element in nums2  
        k = m + n - 1 # Last position in nums1 (where we'll place elements)

        # Merge from the end to avoid overwriting unprocessed elements
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If there are remaining elements in nums2, copy item
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
        # No need to handle remaining elements in nums1 since they're already in place
        