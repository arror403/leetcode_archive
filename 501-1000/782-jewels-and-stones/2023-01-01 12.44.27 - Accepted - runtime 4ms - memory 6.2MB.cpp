class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int res=0;
        for(int i=0;i<jewels.length();i++){
            for(int j=0;j<stones.length();j++){
                if (jewels[i]==stones[j]) res++;
            }
        }
        return res;
    }
};


        // b=0
        // for i in range(0,len(jewels)):
        //     for j in range(0,len(stones)):
        //         if jewels[i]==stones[j]:
        //             b+=1
        
        // return b