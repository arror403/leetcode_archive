class Solution {
public:
    string truncateSentence(string s, int k) {
        string res;
        int x=0;
        for (int i=0;i<s.length();i++){
            if(s[i]!=' ') res+=s[i];
            else if (s[i]==' ') {
                res+=' ';
                x++;
            }
            if (x==k){
                res.erase(res.length()-1);
                break;
            }
        }
        return res;
    }
};