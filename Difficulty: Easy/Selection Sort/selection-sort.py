#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        """
        Sorts an array using the selection sort algorithm.
        
        Args:
            arr (List[int]): The input array to be sorted
        
        Returns:
            List[int]: The sorted array
        
        Raises:
            TypeError: If input is not a list of integers
            ValueError: If input list is empty
        """
        
        # Input validation
        if not isinstance(arr, list):
            raise TypeError("Input must be a list")
        if not arr:
            raise ValueError("Input list cannot be empty")
        if not all(isinstance(x, int) for x in arr):
            raise TypeError("All elements must be integers")
        
        n = len(arr)
        for i in range(n - 1):
            # Find the minimum element in unsorted portion
            min_idx = self._find_minimum_index(arr, i, n)
            
            # Swap if minimum element is not at current postion
            if min_idx != i:
                self._swap_elements(arr, i, min_idx)
        
        return arr
        
    def _find_minimum_index(self, arr: list[int], start: int, end: int) -> int:
        """
        Finds the index of the minimum element in a specified range.
            
        Args:
            arr (List[int]): The input array
            start (int): Starting index of the range
            end (int): Ending index of the range
            
        Returns:
            int: Index of the minimum element
        """
        min_idx = start
        for j in range(start + 1, end):
            if arr[j] < arr[min_idx]:
                min_idx = j
        return min_idx
        
        
    def _swap_elements(self, arr: list[int], i: int, j: int) -> None:
        """
        Swaps two elements in an array.
            
        Args:
            arr (List[int]): The input array
            i (int): Index of first element
            j (int): Index of second element
        """
        arr[i], arr[j] = arr[j], arr[i]


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = [int(i) for i in input().split()]

        obj = Solution()
        obj.selectionSort(arr)

        IntArray().Print(arr)
        print("~")

# } Driver Code Ends