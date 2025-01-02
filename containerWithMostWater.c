int maxArea(int* height, int heightSize) {
    int i = 0;
    int j = heightSize - 1;
    int maxArea = 0;
    while (i<j) {
        int min = (height[i]>height[j]) ? height[j] : height[i];
        int area = (j-i)*min;
        if (area>maxArea){
            maxArea = area;
        }
        if (height[i]<height[j]){
            i++;
        }
        else{
            j--;
        }
    }
    return maxArea;
}