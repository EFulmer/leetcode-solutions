func twoSum(nums []int, target int) []int {
    l := len(nums)
    is := []int{-1, -1}
    for i, v := range nums {
        candidate, goal := i, target-v
        for j := i+1; j < l; j++ {
            if nums[j] == goal {
                is[0] = candidate
                is[1] = j
            }
        }
    }
    return is
}
