class Solution {
    public int countNegatives(int[][] grid) {
        int sum = 0;
        for (int[] row : grid) {
            for (int num : row) {
                if (num < 0) {
                    sum++;
                }
            }
        }
        return sum;
    }
}