impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left_index = 0;
        let mut right_index = height.len() - 1;

        let mut current_max = area(&height, left_index, right_index);
        while left_index < right_index {
            if height[left_index] <= height[right_index] {
                left_index += 1;
            } else {
                right_index -= 1;
            }
            current_max = i32::max(current_max, area(&height, left_index, right_index));
        }

        return current_max;
    }
}

fn area(height: &Vec<i32>, left_index: usize, right_index: usize) -> i32 {
    let base = (right_index - left_index) as i32;
    return base * i32::min(height[left_index], height[right_index]);
}
