class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Find elements that are unique to each list.

        Args:
            nums1: First list of integers
            nums2: Second list of integers
        
        Returns:
            A list containing two lists:
            - Elements in nums1 but not in nums2
            - Elements in nums2 but not in nums1
        """
        set1, set2 = set(nums1), set(nums2)
        return list(set1 - set2), list(set2 - set1)
        