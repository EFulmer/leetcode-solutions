impl Solution {
    // first solution: replace IV with IIII, IX with VIIII, etc.
    // and sum them up using a match case
    // second idea:
    // zip up pairs of (char, next_char);
    // if you have ('I', 'V'), it's 4, ('I', anything_else) is 1...
    pub fn roman_to_int(s: String) -> i32 {
        let s2 = s.replace("IV", "IIII")
                  .replace("IX", "VIIII")
                  .replace("XL", "XXXX")
                  .replace("XC", "LXXXX")
                  .replace("CD", "CCCC")
                  .replace("CM", "DCCCC");
        let mut sum = 0;
        for c in s2.chars() {
            sum += match c {
                'I' => 1,
                'V' => 5,
                'X' => 10,
                'L' => 50,
                'C' => 100,
                'D' => 500,
                'M' => 1000,
                _   => panic!()
            };
        }
        return sum;
    }
}
