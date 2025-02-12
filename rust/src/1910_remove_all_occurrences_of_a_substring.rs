impl Solution {
    pub fn remove_occurrences(s: String, part: String) -> String {
        let part_length = part.len();
        let mut stack: Vec<char> = Vec::with_capacity(s.len());
        for letter in s.chars() {
            stack.push(letter);
            let top_of_stack: String = stack.iter().rev().take(part_length).rev().collect();
            if top_of_stack == part {
                for _ in (0..part_length) {
                    stack.pop();
                }
            }
        }
        let top_of_stack: String = stack.iter().rev().take(part_length).rev().collect();
        if top_of_stack == part {
            for _ in (0..part_length) {
                stack.pop();
            }
        }
        return stack.into_iter().collect();
    }
}
