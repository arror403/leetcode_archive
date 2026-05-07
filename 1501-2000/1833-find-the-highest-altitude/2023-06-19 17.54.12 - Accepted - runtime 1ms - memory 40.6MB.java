class Solution {
    public int largestAltitude(int[] gain) {
        List<Integer> b = new ArrayList<>();
        int x = 0;
        b.add(0);
        
        for (int i = 0; i < gain.length; i++) {
            b.add(x + gain[i]);
            x += gain[i];
        }
        
        return Collections.max(b);
    }
}