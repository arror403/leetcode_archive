class Solution {
    public int findGCD(int[] nums) {
        int maxNum = Arrays.stream(nums).max().getAsInt();
        int minNum = Arrays.stream(nums).min().getAsInt();
        int gcd = gcd(maxNum, minNum);
        return gcd;
    }
    
    private int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
}