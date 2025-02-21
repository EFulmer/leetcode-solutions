int majorityElement(int* nums, int numsSize) {
    int majority;
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (count == 0) {
            majority = nums[i];
        }
        if (majority == nums[i]) {
            count++;
        } else {
            count--;
        }
    }
    return majority;
}
