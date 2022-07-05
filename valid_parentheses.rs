impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut parens = std::collections::HashMap::with_capacity(3);
        parens.insert('(', ')');
        parens.insert('[', ']');
        parens.insert('{', '}');
        let mut closing_parens = std::collections::HashSet::with_capacity(3);
        closing_parens.insert(')');
        closing_parens.insert(']');
        closing_parens.insert('}');

        let mut stack = Vec::new();
        for c in s.chars() {
            if parens.contains_key(&c) == true {
                stack.push(c);
            } else if closing_parens.contains(&c) {
                if stack.len() == 0 {
                    return false;
                } else {
                    let last = stack.pop().unwrap();
                    if parens.get(&last).unwrap() != &c {
                        return false;
                    }
                }
            }
        }

        return stack.len() == 0;
    }
}
