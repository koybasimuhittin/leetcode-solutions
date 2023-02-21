class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        int cnt = 0;
        int lastIndex = nums.size() - 1;
        vector<int> newNums;

        for(int i = 0; i <= lastIndex; i++) {
            if(nums[i] != val) {
                newNums.push_back(nums[i]);
            }
        }
        nums = newNums;
        return nums.size();
    }
};