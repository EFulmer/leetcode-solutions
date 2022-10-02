impl Solution {
    // stdlib version
    pub fn length_of_last_word(s: String) -> i32 {
        let words: Vec<&str> = s.split_whitespace().collect();
        let result = words.last().unwrap().len() as i32;
        return result;
    }
}
