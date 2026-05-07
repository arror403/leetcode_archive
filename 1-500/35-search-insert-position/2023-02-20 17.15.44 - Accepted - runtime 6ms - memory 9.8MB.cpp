class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l=0,r=nums.size()-1,mid;
        while (l<=r){
            mid=int((l+r)/2);
            if (nums[mid]==target) 
                return mid;
            if (nums[mid]<target)
                l=mid+1;
            else 
                r=mid-1;
        }
        return l;
    }
};

        // l , r = 0, len(nums)-1
        // while l <= r:
        //     mid=int((l+r)/2)
        //     if nums[mid]== target:
        //         return mid
        //     if nums[mid] < target:
        //         l = mid+1
        //     else:
        //         r = mid-1
        // return l