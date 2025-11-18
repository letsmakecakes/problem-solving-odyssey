class Solution:
    def largest(self, arr):
        if not arr:
            return None  # or raise ValueError("Array is empty")
        
        largest = arr[0]
        for num in arr:
            if num > largest:
                largest = num
        
        return largest