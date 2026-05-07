class Solution {
    public boolean backspaceCompare(String s, String t) {
        String processedS = processString(s);
        String processedT = processString(t);
        return processedS.equals(processedT);
    }

    private String processString(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c != '#') {
                stack.push(c);
            } else if (!stack.isEmpty()) {
                stack.pop();
            }
        }
        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }
        return sb.toString();
    }
}