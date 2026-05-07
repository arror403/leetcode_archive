class Solution {
    public void sortColors(int[] nums) {
        quicksort(nums,0,nums.length-1);
    }

    public static void quicksort(int[] arr, int left, int right) {
        int i = left, j = right;
        int pivot = arr[(left + right) / 2];
        while (i <= j) {
            while (arr[i] < pivot) {
                i++;
            }
            while (arr[j] > pivot) {
                j--;
            }
            if (i <= j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
        }
        if (left < j) {
            quicksort(arr, left, j);
        }
        if (i < right) {
            quicksort(arr, i, right);
        }
    }
}