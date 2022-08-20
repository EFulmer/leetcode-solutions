use std::collections::HashSet;

impl Solution {
    pub fn first_missing_positive(nums: Vec<i32>) -> i32 {
        let mut numbers: HashSet<i32> = HashSet::with_capacity(nums.len()/2);
        for n in nums {
            if n > 0 {
                numbers.insert(n);
            }
        }
        for i in (1..i32::MAX) {
            if !numbers.contains(&i) {
                return i;
            }
        }
        return i32::MAX;
    }
}
