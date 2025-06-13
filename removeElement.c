int removeElement(int* nums, int numsSize, int val) {
    if (numsSize == 0) {
        return 0;
    }

    int i = 0;
    int j = numsSize - 1;

    while (i <= j) {
        if (nums[i] == val) {
            nums[i] = nums[j];
            j--;
        } else {
            i++;
        }
    }
    return i;
}
