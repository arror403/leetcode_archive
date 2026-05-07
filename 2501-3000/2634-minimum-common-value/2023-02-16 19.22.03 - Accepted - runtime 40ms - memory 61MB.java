class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        Integer[] a = Arrays.stream(nums1)
                                .boxed()
                                .toArray(Integer[]::new);
        Integer[] b = Arrays.stream(nums2)
                                .boxed()
                                .toArray(Integer[]::new);
        Set<Integer> s1 = new HashSet<Integer>(Arrays.asList(a));
        Set<Integer> s2 = new HashSet<Integer>(Arrays.asList(b));
        s1.retainAll(s2);

        Integer[] res = s1.toArray(new Integer[s1.size()]);
        
        if (res.length!=0) return Collections.min(Arrays.asList(res));
        else return -1;
    }
}