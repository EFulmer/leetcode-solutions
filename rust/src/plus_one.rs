impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        // This is just elementary school addition.
        // Start at the right-most number in digits, which is the last, or `digits.len()-1.`
        // From there, add one. If you need to carry one, do so.
        // Keep carrying until you don't need to carry again.

        let mut result = digits.clone();
        let mut n = result.len() - 1;
        let mut carry = 0;
        result[n] += 1;
        if result[n] == 10 {
            result[n] = 0;
            carry = 1;
        } else if 0 <= result[n] && result[n] <= 9 {
            carry = 0;
        } else {
            panic!("Somehow the current digit is not in the range [1, 9] (should never happen)");
        }
        for i in (0..n).rev() {
            result[i] += carry;
            if result[i] == 10 {
                result[i] = 0;
                carry = 1;
            } else if 0 <= result[i] && result[i] <= 9 {
                carry = 0;
            } else {
                panic!("Somehow the current digit is not in the range [1, 9] (should never happen)");
            }
        }
        if carry == 1 {
            // prepend 1 to the start of the vector
            result[0] = 0;
            result.insert(0, 1);
        }
        return result;
    }
}
