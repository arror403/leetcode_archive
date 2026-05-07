class Solution {

//##### power by chatGPT #####

public:
    bool halvesAreAlike(string s) {
        int L = s.length() / 2;
        string a = s.substr(0, L);
        string b = s.substr(L);
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

        int countA = 0, countB = 0;
        for (char ch : a) {
            if (vowels.find(ch) != vowels.end()) {
                countA++;
            }
        }

        for (char ch : b) {
            if (vowels.find(ch) != vowels.end()) {
                countB++;
            }
        }

        return countA == countB;
    }
};