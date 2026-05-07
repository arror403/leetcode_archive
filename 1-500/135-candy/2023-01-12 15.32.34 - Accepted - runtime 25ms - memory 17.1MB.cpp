class Solution {
public:
    int candy(vector<int>& ratings) {
        if(ratings.size()<=1) return ratings.size();
        int candies = 1;
        int up = 0, down = 0, peak = 0;
        for (int i=1;i<ratings.size();i++){
            if (ratings[i-1] < ratings[i]){
                up++;
                peak=up;
                candies+=1+up;
                down=0;       
            }
            else if (ratings[i-1] > ratings[i]){
                down+=1;
                if (peak >= down) candies+=down;
                else candies+=1+down;
                up = 0;    
            }
            else {
                peak = up = down = 0;
                candies += 1;
            }

        }
        return candies;
    }
};
        // if len(ratings) <= 1: 
        //     return len(ratings)
        // candies = 1
        // up = down = peak = 0
        // for i in range(1,len(ratings)):  # ascending
        //     if ratings[i-1] < ratings[i]:
        //         up+=1
        //         peak=up
        //         candies+=1+up
        //         down=0
        //     elif ratings[i-1] > ratings[i]:  # descending
        //         down+=1
        //         candies+=1+down - (1 if peak >= down else 0)
        //         up = 0
        //     else:  # if equal
        //         peak = up = down = 0
        //         candies += 1
        // return candies