impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let n = intervals.len();
        let mut i = 0;
        let mut result = Vec::with_capacity(n);
        let mut my_new_interval = new_interval.clone();
        while i < n && intervals[i][1] < new_interval[0] {
            result.push(intervals[i].clone());
            i += 1;
        }

        while i < n && my_new_interval[1] >= intervals[i][0] {
            my_new_interval[0] = i32::min(my_new_interval[0], intervals[i][0]);
            my_new_interval[1] = i32::max(my_new_interval[1], intervals[i][1]);
            i += 1;
        }
        result.push(my_new_interval);

        while i < n {
            result.push(intervals[i].clone());
            i += 1;
        }

        return result;
    }
}
