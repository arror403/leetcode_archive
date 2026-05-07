class Solution {
public:
    bool isValid(string input) {
        stack<char> s;
        for (char i : input) {
            if (i == '(') {
                s.push('(');
            } else if (i == '[') {
                s.push('[');
            } else if (i == '{') {
                s.push('{');
            } else if (i == ')') {
                if (s.empty()) {
                    return false;
                } else if (s.top() == '(') {
                    s.pop();
                } else {
                    return false;
                }
            } else if (i == ']') {
                if (s.empty()) {
                    return false;
                } else if (s.top() == '[') {
                    s.pop();
                } else {
                    return false;
                }
            } else if (i == '}') {
                if (s.empty()) {
                    return false;
                } else if (s.top() == '{') {
                    s.pop();
                } else {
                    return false;
                }
            }
        }
        return s.empty();
    }
};