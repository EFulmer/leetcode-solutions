impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.len() < 2 {
           return 1;
        }
        let mut current_index = 0;
        let mut next_index = 1;
        while next_index < nums.len() {
            // check if current and next match
            // (clearly unsafe, should be doing if let or unwrap with a sentinel value etc. but it's okay in this context)
            if nums[current_index] == nums[next_index] {
                // remove next if they do
                nums.remove(next_index);
            } else {
                // if not, advance both
                current_index += 1;
                next_index += 1;
            }
        }
        return nums.len() as i32;
    }
}
