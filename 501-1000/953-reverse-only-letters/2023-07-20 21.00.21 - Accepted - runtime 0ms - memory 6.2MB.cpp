class Solution {
public:
    string reverseOnlyLetters(string s) {
        string t;
        string res;
        int x = 0;
        int j = 0;
        for (char i : s) {
            if (isalpha(i)) {
                t.push_back(i);
            }
        }

        reverse(t.begin(), t.end());

        for (int Q = 0; Q < s.length(); ++Q) {
            if (isalpha(s[x])) {
                res.push_back(t[j]);
                j++;
            }
            else {
                res.push_back(s[x]);
            }
            x++;
        }

        return res;
    }
};