use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_counter = HashMap::new();
        let mut t_counter = HashMap::new();

        for c in s.chars() {
            let count = s_counter.entry(c).or_insert(0);
            *count += 1;
        }
        for c in t.chars() {
            let count = t_counter.entry(c).or_insert(0);
            *count += 1;
        }

        return s_counter == t_counter;
    }
}
