class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(list1, list2):
            combined = []
            i, j = 0, 0

            while i < len(list1) and j < len(list2):
                if list1[i] < list2[j]:
                    combined.append(list1[i])
                    i += 1
                else:
                    combined.append(list2[j])
                    j += 1
            
            combined.extend(list1[i:])
            combined.extend(list2[j:])
            return combined
        
        combined_list = merge(nums1, nums2)
        n = len(combined_list)

        if n % 2 == 1:
            return combined_list[n // 2]
        else:
            mid = n // 2
            return (combined_list[mid - 1] + combined_list[mid]) / 2