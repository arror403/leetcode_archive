class Solution {
public:
    bool isSubsequence(string t, string s) {
        bool f=false;
        int x=0;
        if (t.length() > s.length()) return 0;
        if (t.length()==0) return 1;
        else{
            for (int i=0;i<s.length();i++){
                if (x<s.length() && t[x]==s[i]) x++;
                if (x==t.length()){
                    f=true;
                    break;
                }
            }
        }
        return f;
    }
};

        // f=False
        // x=0
        // if len(t)>len(s):
        //     return 0
        // if len(t) == 0:
        //     return 1
        // else:
        //     for i in s:
        //         if x<len(s) and t[x]==i:
        //             x+=1
        //         if x==len(t):
        //             f=True
        //             break
        // return f