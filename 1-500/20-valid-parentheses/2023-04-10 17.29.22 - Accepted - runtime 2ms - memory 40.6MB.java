class Solution {
    public boolean isValid(String input) {
        Stack<Character> s = new Stack<>();
        for (char i : input.toCharArray()) {
            if (i == '(') {
                s.push('(');
            } else if (i == '[') {
                s.push('[');
            } else if (i == '{') {
                s.push('{');
            } else if (i == ')') {
                if (s.isEmpty()) {
                    return false;
                } else if (s.peek() == '(') {
                    s.pop();
                } else {
                    return false;
                }
            } else if (i == ']') {
                if (s.isEmpty()) {
                    return false;
                } else if (s.peek() == '[') {
                    s.pop();
                } else {
                    return false;
                }
            } else if (i == '}') {
                if (s.isEmpty()) {
                    return false;
                } else if (s.peek() == '{') {
                    s.pop();
                } else {
                    return false;
                }
            }
        }
        return s.isEmpty();
    }
}