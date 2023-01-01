use std::collections::HashMap;

impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        // First check: if the pattern and the list of words (after splitting) are of different length, we can abort immediately.
        let words: Vec<String> = s.split_whitespace().map(String::from).collect();
        if words.len() != pattern.len() {
            return false;
        }
        let mut pattern_to_word: HashMap<char, String> = HashMap::with_capacity(pattern.len());
        let mut word_to_pattern: HashMap<String, char> = HashMap::with_capacity(words.len());
        for (pattern_variable, word) in pattern.chars().zip(words.iter()) {
            // Check if the word is assigned to another pattern already
            if let Some(old_word) = pattern_to_word.insert(pattern_variable, word.to_string()) {
                if old_word != *word {
                    return false;
                }
            } else if let Some(old_pattern) = word_to_pattern.insert(word.to_string(), pattern_variable) { // insertion of a brand new key to P->W was successful, check if inserting W->P overwrites another
                if old_pattern != pattern_variable {
                    return false;
                }
            }
        }
        return true;
    }
}
