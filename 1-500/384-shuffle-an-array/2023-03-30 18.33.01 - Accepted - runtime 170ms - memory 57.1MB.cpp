class Solution {
private:
    vector<int> original;
public:
    Solution(vector<int>& nums) {
        original = nums;
    }

    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return original;
    }

    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> shuffled = original;
        random_device rd;
        mt19937 g(rd());
        ::shuffle(shuffled.begin(), shuffled.end(), g);
        return shuffled;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */