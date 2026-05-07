class Solution {
public:
    int lengthOfLastWord(string s) {
        istringstream in (s);
        vector <string> v;

        string t;
        while ( in >> t) {
            v.push_back(t);
        }

        return v[v.size()-1].length();

    }
};