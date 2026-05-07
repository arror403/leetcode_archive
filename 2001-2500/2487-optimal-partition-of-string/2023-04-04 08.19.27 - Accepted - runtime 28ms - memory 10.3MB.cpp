class Solution {
public:
    int partitionString(string s) {
        vector<int> m(26);
        int ans = 0;
        for (char c : s) {
            if (++m[c - 'a'] == 1) continue;
            fill(m.begin(), m.end(), 0);
            m[c - 'a'] = 1;
            ans++;
        }
        return ans + 1;   
    }
};