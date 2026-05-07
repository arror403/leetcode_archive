class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums); // Sort the input array to handle duplicates
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, used, current, res);
        return res;
    }

    private void backtrack(int[] nums, boolean[] used, List<Integer> current, List<List<Integer>> res) {
        if (current.size() == nums.length) {
            res.add(new ArrayList<>(current));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) {
                continue;
            }

            used[i] = true;
            current.add(nums[i]);
            backtrack(nums, used, current, res);
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }
}