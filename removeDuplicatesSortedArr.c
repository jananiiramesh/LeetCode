
int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) return 0;  

    int k = 1;  
    int new = 1;  
    int iterate = 1;  
    int val = nums[0];  

    while (iterate < numsSize) {
        while (iterate < numsSize && nums[iterate] == val) {
            iterate++;
        }

        if (iterate < numsSize) {
            nums[new] = nums[iterate];
            new++;
            k++;
            val = nums[iterate]; 
        }
    }
    
    return k;
}
