public class Solution {
    public int uniquePaths(int m, int n) {
        int[] cur = new int[n];
        
        // Initialize the first row with 1
        for (int i = 0; i < n; i++) {
            cur[i] = 1;
        }
        
        // Calculate unique paths using dynamic programming
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                cur[j] += cur[j - 1];
            }
        }
        
        return cur[n - 1];
    }
}