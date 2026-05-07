class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int M = -1;
        List<Boolean> output = new ArrayList<>();
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] > M) {
                M = candies[i];
            }
        }
        
        for (int i = 0; i < candies.length; i++) {
            if ((candies[i] + extraCandies) >= M) {
                output.add(true);
            } else {
                output.add(false);
            }
        }
        return output;
    }
}