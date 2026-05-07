public class Solution {
    public boolean strongPasswordCheckerII(String password) {
        String m = "!@#$%^&*()-+";
        boolean b;
        
        if (password.length() < 8) return false;
        
        b = false;
        for (char i : password.toCharArray()) {
            if (Character.isLowerCase(i)) {
                b = true;
                break;
            }
        }
        if (!b) return false;
        
        b = false;
        for (char i : password.toCharArray()) {
            if (Character.isUpperCase(i)) {
                b = true;
                break;
            }
        }
        if (!b) return false;
        
        b = false;
        for (char i : password.toCharArray()) {
            if (Character.isDigit(i)) {
                b = true;
                break;
            }
        }
        if (!b) return false;
        
        b = false;
        for (char i : password.toCharArray()) {
            for (char j : m.toCharArray()) {
                if (i == j) {
                    b = true;
                    break;
                }
            }
        }
        if (!b) return false;
        
        for (int i = 0; i < password.length() - 1; i++) {
            if (password.charAt(i) == password.charAt(i + 1))
                return false;
        }
        
        return true;
    }
}