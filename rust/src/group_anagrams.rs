use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut ht: HashMap<String, Vec<String>> = HashMap::new();
        for s in strs.iter() {
            let s_sorted = Solution::sort_string(s.to_string());
            let mut anagrams = ht.get_mut(&s_sorted);
            if anagrams.is_some() {
                anagrams.unwrap().push(s.to_string());
            } else {
                ht.insert(s_sorted, vec![s.to_string()]);
            }
        }
        let mut result = Vec::with_capacity(ht.len());
        for v in ht.values() {
            result.push(v.to_vec());
        }
        return result;
    }

    fn sort_string(s: String) -> String {
        let mut char_vec = s.chars().collect::<Vec<char>>();
        char_vec.sort();
        let s_sorted = char_vec.into_iter().collect::<String>();
        return s_sorted;
    }
}
