class Solution {
public:
    bool isPalindrome(int x) {
        auto s = to_string(x);
        // cout << s;
        return palindrome(s);
    }

    bool palindrome(string s){
        for (int i=0; i<s.length()/2; ++i){
            if (s[i] != s[s.length()-1-i])
                return false;
        }
        return true;
    }

};