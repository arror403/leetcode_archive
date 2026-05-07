class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for (auto i:words){
            if (isPalindrome(i)){
                return i;
            }
        }
        return "";
    }
    bool isPalindrome(string S){
        // Stores the reverse of the
        // string S
        string P = S;
        // Reverse the string P
        reverse(P.begin(), P.end());
        // If S is equal to P
        return S==P;
    }    
};