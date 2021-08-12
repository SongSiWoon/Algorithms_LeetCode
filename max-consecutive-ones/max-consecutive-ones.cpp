class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int cnt = 0;
        int result = 0;
        for(int i = 0; i<nums.size(); i++){
            if(nums[i] == 1){
                cnt ++;
                result = std::max(result,cnt);
            }
            else{
                cnt = 0;
            }
        }
        return result;
    }
};