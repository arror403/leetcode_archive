class Solution {
public:
    bool checkPowersOfThree(int n) {
        vector<int> r;
        while (n>=3){
            r.push_back(n%3);
            n/=3;
        }
        r.push_back(n);
        for(int i=0;i<r.size();i++){
            if (r[i]==1 || r[i]==0) continue;
            else return false;
        }
        return true;
    }
};


        // r=[]
        // while n>=3:
        //     r.append(n%3)
        //     n//=3
        // r.append(n)
        // # r.reverse()
        
        // for i in r:
        //     if i==1 or i==0: continue
        //     else: return False
        
        // return True