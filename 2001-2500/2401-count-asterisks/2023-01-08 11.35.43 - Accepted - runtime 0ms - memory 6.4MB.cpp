class Solution {
public:
    int countAsterisks(string s) {
        int res=0,c=0;
        for (int i=0;i<s.length();i++){
            if (s[i]=='|') c++;
            if (c%2==0 && s[i]=='*') res++;
        }
        return res;
    }
};

        // res,c=0,0
        // for i in list(s):
        //     if i=='|': c+=1
        //     if c%2==0 and i=='*': res+=1
        // return res