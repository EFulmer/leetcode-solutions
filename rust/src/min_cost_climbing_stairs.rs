impl Solution {
    fn min(m: i32, n: i32) -> i32 {
        if m > n {
            return n;
        }
        return m;
    }
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut current_minimum_cost = 0;
        let mut candidate_1 = cost[0];
        let mut candidate_2 = cost[1];
        for i in 2..cost.len() {
            current_minimum_cost = cost[i] + Solution::min(candidate_1, candidate_2);
            candidate_1 = candidate_2;
            candidate_2 = current_minimum_cost;
        }
        return Solution::min(candidate_1, candidate_2);
    }
}
