int max3(int x, int y, int z) {
    if ((x > y) && (x > z)) {
        return x;
    } else if ((y > x) && (y > z)) {
        return y;
    } else {
        return z;
    }
}

int longestMonotonicSubarray(int* nums, int numsSize) {
    int longest_increasing;
    int longest_decreasing;
    int max_length;

    longest_increasing = 1;
    longest_decreasing = 1;
    max_length = 1;

    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] > nums[i+1]) {
            longest_decreasing += 1;
            longest_increasing = 1;
        } else if (nums[i] < nums[i+1]) {
            longest_increasing += 1;
            longest_decreasing = 1;
        } else {
            longest_increasing = 1;
            longest_decreasing = 1;
        }
        max_length = max3(longest_increasing, longest_decreasing, max_length);
    }

    return max_length;
}
