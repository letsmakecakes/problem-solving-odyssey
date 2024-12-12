def rearrange(input_arr):
    """
    Rearranges the given array in-place to move all negative numbers
    to the beginning and positive numbers to the end while maintaining
    their relative order.

    Parameters:
    arr (list): The input array containing both negative and positive integers.

    Returns:
    None: The function modifies the input array in-place.

    Example:
    Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
    Output: -12 -13 -5 -7 -3 -6 11 6 5
    """
    left = 0
    right = 0
    while right < len(input_arr):
        if input_arr[right] < 0:
            input_arr[right], input_arr[left] = input_arr[left], input_arr[right]
            left += 1
        right += 1


arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
print("Before rearranging: ", arr)
rearrange(arr)
print("After rearranging: ", arr)
