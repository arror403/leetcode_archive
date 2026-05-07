class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        //##### power by chatGPT #####
        string m = "123456789";
        int l = to_string(low).length();
        int h = to_string(high).length();
        vector<int> res;

        for (int i = l; i <= h; ++i) {
            for (int j = 0; j <= 9 - i; ++j) {
                string num_str = m.substr(j, i);
                int num = stoi(num_str);
                if (low <= num && num <= high) res.push_back(num);
                
            }
        }
        
        sort(res.begin(), res.end());
        return res;
    }
};