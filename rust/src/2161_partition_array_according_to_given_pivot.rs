impl Solution {
    pub fn pivot_array(nums: Vec<i32>, pivot: i32) -> Vec<i32> {
        let mut result = Vec::with_capacity(nums.len());
        let mut less_than = 0;
        let mut pivot_count = 0;
        let mut greater_than = 0;

        for num in &nums {
            if *num == pivot {
                pivot_count += 1;
            } else if *num < pivot {
                less_than += 1;
            } else {
                greater_than += 1;
            }
            // Need to size the vector up, capacity != size.
            result.push(0);
        }

        let pivot_start = less_than;
        let gt_start = less_than + pivot_count;
        let mut li_index = 0;
        let mut pivot_index = pivot_start;
        let mut gt_index = gt_start;

        for num in &nums {
            if *num == pivot {
                result[pivot_index] = *num;
                pivot_index += 1;
            } else if *num < pivot {
                result[li_index] = *num;
                li_index += 1;
            } else {
                result[gt_index] = *num;
                gt_index += 1;
            }
        }

        return result;
    }
}
