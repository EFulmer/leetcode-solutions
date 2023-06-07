use std::collections::BinaryHeap;
use std::iter::FromIterator;

impl Solution {
    pub fn min_stone_sum(piles: Vec<i32>, k: i32) -> i32 {
        // Basically, at any step, we want to get the biggest pile, halve it, and update its count.

        let mut piles: BinaryHeap<i32> = BinaryHeap::from(piles);
        let mut k = k;
        while k > 0 {
            let current_max = piles.pop().unwrap(); // unwrap is safe in this context because of the guarantee that `piles` passed in to us is of len >= 1; if it panics, it's because I messed up.
            let to_remove = current_max / 2;
            piles.push(current_max - to_remove);
            k -= 1;
        }
        return piles.iter().sum();
    }
}
