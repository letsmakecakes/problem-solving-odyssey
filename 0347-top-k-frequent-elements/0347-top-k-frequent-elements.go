import (
    "sort"
)

func topKFrequent(nums []int, k int) []int {
    freqMap := make(map[int]int)
    
    for _, num := range nums {
        freqMap[num]++
    }

    unique := make([]int, 0, len(freqMap))
    for num := range freqMap {
        unique = append(unique, num)
    }

    sort.Slice(unique, func(i, j int) bool {
        return freqMap[unique[i]] > freqMap[unique[j]]
    })

    return unique[:k]
}