impl Solution {
    pub fn detect_capital_use(word: String) -> bool {
        let title_case = (word.chars().nth(0).unwrap().is_uppercase()) &
            // This slicing is safe since the LC input will be ASCII only
            // In real project code I would probably use an external crate or extend this over
            // multiple lines (maybe by creating a Chars iterator and then advancing it by one)?
            (word[1..].chars().all(|c| c.is_lowercase()));
        let all_uppercase = word.chars().all(|c| c.is_uppercase());
        let all_lowercase = word.chars().all(|c| c.is_lowercase());
        return title_case || all_uppercase || all_lowercase;
    }
}
