class Solution {
public:
    vector<int> topKFrequent(std::vector<int>& nums, int k) {
        vector<int> res;
        
        // Count the frequency of each number
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        // Create a vector of pairs (number, frequency)
        vector<pair<int, int>> freqList;
        for (auto& entry : count) {
            freqList.push_back(entry);
        }
        
        // Sort the vector based on frequency in descending order
        sort(freqList.begin(), freqList.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second > b.second;
        });
        
        // Get the top k frequent elements
        for (int i = 0; i < k; i++) {
            res.push_back(freqList[i].first);
        }
        
        return res;
    }
};