class Solution {
    public int partitionString(String s) {
        int[] m = new int[26];
        int ans = 0;
        for (char c : s.toCharArray()) {
            if (++m[c - 'a'] == 1) continue;
            Arrays.fill(m, 0);
            m[c - 'a'] = 1;
            ans++;
        }
        return ans + 1;        
    }
}