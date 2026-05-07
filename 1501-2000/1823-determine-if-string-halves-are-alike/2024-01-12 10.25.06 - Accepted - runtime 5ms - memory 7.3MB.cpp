class Solution {
public:
    bool halvesAreAlike(string s) {
        int L = s.length() / 2;
        string a = s.substr(0, L);  // Use string_view for efficiency
        string b = s.substr(L);

        bitset<10> vowels;  // Assuming ASCII characters, adjust size if needed
        vowels['a'] = vowels['e'] = vowels['i'] = vowels['o'] = vowels['u'] = true;
        vowels['A'] = vowels['E'] = vowels['I'] = vowels['O'] = vowels['U'] = true;

        int count = 0;
        for (int i=0; i<L; i++) {
            if (vowels[a[i]]) {
                count++;
            }
            if (vowels[b[i]]) {
                count--;
            }
        }

        return count==0;
    }
};