class Solution {
public:
    string largestGoodInteger(string num) {
        string res;
        for (int i = 0; i < num.length() - 2; i++) {
            if (num[i] == num[i + 1] && num[i] == num[i + 2]) {
                res.push_back(num[i]);
            }
        }

        if (res.empty()) {
            return "";
        }

        char r = *max_element(res.begin(), res.end());

        return string(3, r);
    }
};