class Solution {
public:
    string toLowerCase(string s){
        string res;
        for(int i=0;i<s.length();i++){
            res+=tolower(s[i]);            
        }
        return res;
    }
};