func topKFrequent(nums []int, k int) []int {
    if len(nums) == 0 || k == 0 {
        return []int{}
    }

    // Count frequencies
    freqMap := make(map[int]int)
    for _, num := range nums {
        freqMap[num]++
    }

    // Create buckets where index represents frequency
    buckets := make([][]int, len(nums)+1)
    for num, freq := range freqMap {
        buckets[freq] = append(buckets[freq], num)
    }

    // Collect top k elements from highest frequency buckets
    result := make([]int, 0, k)
    for i := len(buckets) - 1; i >= 0 && len(result) < k; i-- {
        for _, num := range buckets[i] {
            if len(result) < k {
                result = append(result, num)
            } else  {
                break
            }
        }
    }

    return result
}