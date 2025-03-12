#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
 
    def mergeSort(self, array, start_index, end_index):
        if start_index < end_index:
            middle_index = (start_index + end_index) // 2
            self.mergeSort(array, start_index, middle_index)
            self.mergeSort(array, middle_index + 1, end_index)
            self.merge(array, start_index, middle_index, end_index)
            
    
    def merge(self, array, start_index, middle_index, end_index):
        left_subarray = array[start_index:middle_index + 1]
        right_subarray = array[middle_index + 1:end_index + 1]
        
        left_position = 0
        right_position = 0
        array_position = start_index
        
        # Merge elements from both subarrays in sorted order
        while left_position < len(left_subarray) and right_position < len(right_subarray):
            if left_subarray[left_position] <= right_subarray[right_position]:
                array[array_position] = left_subarray[left_position] 
                left_position += 1
            else:
                array[array_position] = right_subarray[right_position]
                right_position += 1
            array_position += 1
        
        # Copy remaining elements from left subarray if any
        while left_position < len(left_subarray):
            array[array_position] = left_subarray[left_position]
            left_position += 1
            array_position += 1
        
        # Copy remaining elements from right subarray if any
        while right_position < len(right_subarray):
            array[array_position] = right_subarray[right_position]
            right_position += 1
            array_position += 1

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends