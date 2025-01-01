use std::cmp;

impl Solution {
    pub fn max_score(s: String) -> i32 {
        let total_ones: i32 = s.chars().filter(|&c| c == '1').count().try_into().unwrap();
        let mut current_zeroes = 0;
        let mut current_ones = total_ones;
        let mut result = 0;
        for (i, c) in s.chars().enumerate() {
            if i == s.len() - 1 {
                break;
            }
            if c == '1' {
                current_ones -= 1;
            } else {
                current_zeroes += 1;
            }
            result = cmp::max(result, current_ones + current_zeroes);
        }
        return result;
    }
}
