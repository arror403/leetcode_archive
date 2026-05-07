class Solution {
public:
    bool strongPasswordCheckerII(string password) {
        string m="!@#$%^&*()-+";
        bool b;
        if (password.length()<8) return false;
        b=false;
        for (char i:password){
            if (islower(i)){
                b=true;
                break;
            }
        }
        if (b==false) return false;
        b=false;
        for (char i:password){
            if (isupper(i)){
                b=true;
                break;
            }
        }
        if (b==false) return false;
        b=false;
        for (char i:password){
            if (isdigit(i)){
                b=true;
                break;
            }
        }
        if (b==false) return false;
        b=false;
        for (char i:password){
            for (char j:m){
                if (i==j){
                    b=true;
                    break;
                }
            }
        }
        if (b==false) return false;
        for (int i=0;i<password.length()-1;i++){
            if (password[i]==password[i+1])
                return false;
        }
        return true;  
    }
};

