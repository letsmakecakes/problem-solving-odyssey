class Solution:
    def leaders(self, arr):
        n  = len(arr)
        array_leaders = list()
        max_from_right = arr[-1]
        array_leaders.append(max_from_right)
        
        # Traverse from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right :
                array_leaders.append(arr[i])
                max_from_right  = arr[i]
        
        
        return array_leaders[::-1]
            