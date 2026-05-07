class Solution {
public:
    bool backspaceCompare(string s, string t) {
        string processedS = processString(s);
        string processedT = processString(t);
        return processedS == processedT;
    }

private:
    string processString(string s) {
        stack<char> st;
        for (char c : s) {
            if (c != '#') {
                st.push(c);
            } else if (!st.empty()) {
                st.pop();
            }
        }
        string processed = "";
        while (!st.empty()) {
            processed += st.top();
            st.pop();
        }
        reverse(processed.begin(), processed.end());
        return processed;
    }       
};