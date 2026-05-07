class Solution {
    public int diagonalSum(int[][] mat) {
        int l = mat[0].length;
        int sum = 0;
        for (int i = 0; i < l; i++) {
            sum += mat[i][i];
        }
        for (int i = l - 1; i >= 0; i--) {
            if ((l - i - 1) != i) {
                sum += mat[l - i - 1][i];
            }
        }
        return sum;
    }
}