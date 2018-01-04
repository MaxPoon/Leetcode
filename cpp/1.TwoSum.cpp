class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            int number = nums[i];
            int numberToFind = target - number;
            if (hash.find(numberToFind) != hash.end()) {
                result = {i, hash[numberToFind]};
                return result;
            }
            hash[nums[i]] = i;
        }
        return result;
    }
};
