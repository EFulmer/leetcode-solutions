impl Solution {
    fn helper(x: f64, n: i32) -> f64 {
        let mut res = 1.0;
        let mut i = n.abs();
        let mut x = x;
        while i > 0 {
            if i % 2 == 0 {
                x *= x;
                i /= 2;
            } else {
                res *= x;
                i -= 1;
            }
        }
        if n < 0 {
            return 1.0 / res;
        }
        return res;
    }
    pub fn my_pow(x: f64, n: i32) -> f64 {
        // match against the constants
        match n {
            0 => return 1.0,
            1 => return x,
            // TODO this is ugly
            i32::MIN => match x as i32 {
                -1 => return 1.0,
                1 => return x,
                _  => return 0.0,
            }
            _ => return Self::helper(x, n),
        }

    }
}
