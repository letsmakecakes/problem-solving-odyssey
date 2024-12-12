def reverse_array(nums: list) -> list:
    """
    Reverses the elements of the given list in place.

    Args:
        nums (list): A list of elements to be reversed.

    Returns:
        list: The same list with elements in reverse order.
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums

# Test the reverse_array function
nums = [1, 4, 3, 2, 6, 5]
print("Before reversing: ", nums)
nums = reverse_array(nums)
print("After reversing: ", nums)
