int max(int x, int y) {
    if (x > y) {
        return x;
    }
    return y;
}

int maxSubArray(int* nums, int numsSize) {
    int best_sum = -65536;
    int current_sum = 0;
    for (int i = 0; i < numsSize; i++) {
        current_sum = max(current_sum + nums[i], nums[i]);
        best_sum = max(current_sum, best_sum);
    }
    return best_sum;
}
