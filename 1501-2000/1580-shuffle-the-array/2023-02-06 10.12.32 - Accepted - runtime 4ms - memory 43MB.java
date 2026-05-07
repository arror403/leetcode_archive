class Solution {
    public int[] shuffle(int[] nums, int n) {
        ArrayList<Integer> b=new ArrayList<>();
        int index = n;
        for(int i=0;i<n;i++){
            b.add(nums[i]);
            b.add(nums[index]);
            index++;
        }
        int[] arr = b.stream().mapToInt(i -> i).toArray();
        return arr;
    }
}