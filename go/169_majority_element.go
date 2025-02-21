func majorityElement(nums []int) int {
    maj := 0
    count := 0
    for _, num := range nums {
        if count == 0 {
            maj = num
        }
        if maj == num {
            count++
        } else {
            count--
        }
    }
    return maj
}
