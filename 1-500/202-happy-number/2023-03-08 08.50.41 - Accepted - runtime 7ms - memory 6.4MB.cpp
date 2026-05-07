class Solution {
public:
    bool isHappy(int n) {
        int loop_time=0,sum;
        vector<int> t;
        while (1){
            loop_time++;
            sum=0;
            t=toVector(n);
            for(auto i:t)
                sum+=pow(i,2);
            if (sum==1){
                return 1;
                break;
            }
            else{
                n=sum;
                if (loop_time==10){
                    return 0;
                    break;
                }
            }
        }
    }
    vector<int> toVector(int x){
        vector<int> numbers;
        while(x>0){
        numbers.push_back(x%10);
        x/=10;
        }
        reverse(numbers.begin(), numbers.end());
        return numbers;
    }
};