class Solution:
    def frequencyCount(self, arr):
        count_map = {}
        for num in arr:
            count_map[num] = count_map.get(num, 0) + 1
        
        return [count_map.get(i, 0) for i in range(1, len(arr) + 1)]
