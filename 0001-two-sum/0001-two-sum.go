func twoSum(nums []int, target int) []int {
    seen := make(map[int]int, len(nums))

    for i, num := range nums {
        if prevIndex, exists := seen[target-num]; exists {
            return []int{prevIndex, i}
        }
        seen[num] = i
    }

    return nil // No solution found
}