func twoSum(nums []int, target int) []int {
	numsMap := make(map[int]int)

	for i, num := range nums {
		complement := target - num
		if prevIndex, ok := numsMap[complement]; ok {
			return []int{prevIndex, i}
		}

		numsMap[num] = i
	}

	return nil
}