class Solution {
public:
    string capitalizeTitle(string title) {
    vector<string> words;
    string word = "";
    for (char c : title) {
        if (c == ' ') {
            words.push_back(word);
            word = "";
        } else {
            word += c;
        }
    }
    words.push_back(word);
    string capitalized_title = "";
    for (string word : words) {
        if (word.length() <= 2) {
            for (char c : word) {
                capitalized_title += tolower(c);
            }
        } else {
            capitalized_title += toupper(word[0]);
            for (int i = 1; i < word.length(); i++) {
                capitalized_title += tolower(word[i]);
            }
        }
        capitalized_title += " ";
    }
    capitalized_title.pop_back(); // remove trailing space
    return capitalized_title;
    }
};