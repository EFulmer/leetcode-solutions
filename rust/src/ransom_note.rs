impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut map: Vec<u32> = Vec::with_capacity(26);
        for i in 0..26 {
            map.push(0);
        }
        // populate the "hash-map" with all the characters from magazine
        for c in magazine.chars() {
            // safe since we know all the characters will be 'a'..'z'
            let code_point: usize = ((c as u32) % 97) as usize;
            map[code_point] += 1;
        }
        // then iterate over ransom_note and subtract
        for c in ransom_note.chars() {
            let code_point: usize = ((c as u32) % 97) as usize;
            if map[code_point] <= 0 {
                return false;
            }
            map[code_point] -= 1;
        }
        // if any index would be negative, immediately return false
        return true;
    }
}
