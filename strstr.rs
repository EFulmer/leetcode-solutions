impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let n = needle.len();
        let h = haystack.len();
        for i in (0..h) {
            if i + n > h {
                break;
            }
            if haystack[i..(i+n)] == needle {
                return i as i32;
            }
        }
        return -1;
    }
}
