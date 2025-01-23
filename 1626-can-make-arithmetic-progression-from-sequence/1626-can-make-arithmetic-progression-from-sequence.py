class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr_sorted = sorted(arr)
        d = arr_sorted[1] - arr_sorted[0]

        for i in range(1, len(arr_sorted) - 1):
            if arr_sorted[i + 1] - arr_sorted[i] != d:
                return False
        
        return True
