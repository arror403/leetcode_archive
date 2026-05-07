class Solution {
public:
    string largestOddNumber(string num) {
        for(int i=num.size()-1;i>=0;i--){
            int tmp=int(num[i])-48;
            if (tmp%2==0) continue;
            return num.substr(0,i+1);
        }
        return "";
    }
};

        // for i in range(len(num)-1,-1,-1):
        //     # print(i)
        //     if int(num[i])%2==0: continue
        //     return num[0:i+1]
                
        // return ""