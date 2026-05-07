class Solution {
    public int maximumCount(int[] nums) {
        int x = 0, y = 0;
        for (int i : nums) {
            if (i > 0)
                x += 1;
            else if (i < 0)
                y += 1;
        }
        return Math.max(x, y);
    }
}