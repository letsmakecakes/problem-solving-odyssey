class Solution: 
    def selectionSort(self, arr):
        arr_size = len(arr)
        for i in range(arr_size - 1):
            min_idx = i
            for j in range(i + 1, arr_size):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if i != min_idx:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]