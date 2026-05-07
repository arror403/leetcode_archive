class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int> hashmap;
        vector<int> result;
        
        for (int i = 0; i < numbers.size(); i++) {
            int complement = target - numbers[i];
            
            if (hashmap.find(complement) != hashmap.end()) {
                result.push_back(hashmap[complement]);
                result.push_back(i + 1);
                break;
            }
            
            hashmap[numbers[i]] = i + 1;
        }
        
        return result;
    }
};