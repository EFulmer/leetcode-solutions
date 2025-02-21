impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut maj = 0;
        let mut count = 0;
        for num in &nums {
            if count == 0 {
                maj = *num;
            }
            if maj != *num {
                count -= 1;
            } else {
                count += 1;
            }
        }
        return maj;
    }
}
