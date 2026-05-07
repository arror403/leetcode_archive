class Solution {
public:
    int countDigitOne(int n) {
        int ones = 0;
        long long m = 1;
        while (m <= n) {
            int a = n / m;
            int b = n % m;
            ones += (a + 8) / 10 * m;
            if (a % 10 == 1) {
                ones += b + 1;
            }
            m *= 10;
        }
        return ones;
    }
};