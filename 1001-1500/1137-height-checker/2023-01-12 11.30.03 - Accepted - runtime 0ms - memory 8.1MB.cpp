class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> r=heights;
        sort(heights.begin(), heights.end());
        int res=0;
        for (int i=0;i<heights.size();i++){
            if (heights[i]!=r[i]) res++;
        }
        return res;
    }
};

        // r=sorted(heights)
        // res=0
        // for i in range(len(heights)):
        //     if heights[i]!=r[i]:
        //         res+=1

        // return res