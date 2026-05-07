class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binary_search(nums,0,nums.size()-1,target);
    }
        
    int binary_search(vector<int>& arr,int low,int high,int x){
            // # Check base case
            if (high >= low){

                int mid = (high + low)/2;

                // # If element is present at the middle itself
                if (arr[mid] == x)
                    return mid;

                // # If element is smaller than mid, then it can only
                // # be present in left subarray
                else if (arr[mid] > x)
                    return binary_search(arr, low, mid - 1, x);

                // # Else the element can only be present in right subarray
                else
                    return binary_search(arr, mid + 1, high, x);
            }

            else
                // # Element is not present in the array
                return -1;
    }
};