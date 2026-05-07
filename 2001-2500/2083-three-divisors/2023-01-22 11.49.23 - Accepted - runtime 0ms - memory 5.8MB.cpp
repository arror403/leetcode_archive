class Solution {
public:
    bool isThree(int n) {
        int re=0;
        for (int i=1;i<=n+1;i++){
            if ((n%i)==0) re++;
            if (re>3) break;
        }
        return re==3;
    }
};



        // re=0
        // for i in range(1,n+1):
        //     # print(i)
        //     if (n%i)==0:
        //         re+=1
        //     if re>3:
        //         break
                
        // if re==3:
        //     return 1
        // else:
        //     return 0