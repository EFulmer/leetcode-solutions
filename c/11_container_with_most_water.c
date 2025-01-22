int max(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

int min(int a, int b) {
    if (a < b) {
        return a;
    }
    return b;
}

int area(int* height, int start_index, int end_index) {
    return (end_index - start_index) * min(height[start_index], height[end_index]);
}

int maxArea(int* height, int heightSize) {
    int start_index = 0;
    int end_index = heightSize - 1;
    int current_max = area(height, start_index, end_index);
    while (start_index < end_index) {
        if (height[start_index] <= height[end_index]) {
            start_index += 1;
        } else {
            end_index -= 1;
        }
        current_max = max(current_max, area(height, start_index, end_index));
    }
    return current_max;
}
