class Solution {
public:
    char repeatedCharacter(string s) {
        unordered_map<char, int> counts;
        
        for (char c : s) {
            counts[c]++;
            if (counts[c] == 2) {
                return c;
            }
        }
        
        return '\0'; // Return null character if no duplicates found        
    }
};