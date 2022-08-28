struct NumArray {
    range: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {

    fn new(nums: Vec<i32>) -> Self {
        let mut iter = nums.iter().scan(0, |acc, &n| {
            *acc = *acc + n;
            Some(*acc)
        });
        return NumArray {range: iter.collect()};
    }

    fn sum_range(&self, left: i32, right: i32) -> i32 {
        if left > right {
            panic!(
                format!("left bound must be strictly less than right bound but sum_range was called with {0} and {1}", left, right)
            );
        }
        if left == 0 {
            return self.range[right as usize];
        }
        return self.range[right as usize] - self.range[(left-1) as usize];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * let ret_1: i32 = obj.sum_range(left, right);
 */
