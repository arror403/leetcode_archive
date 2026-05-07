class Solution {
public:
    bool isPalindrome(string s) {
        string p="",q="";
        for (int i=0;i<s.length();i++){
            if (isalnum(s[i]))
                p+=s[i];
        }        
        for (int i=p.length()-1;i>=0;i--)
            q+=p[i];
        
        transform(p.begin(), p.end(), p.begin(), [](unsigned char c){ return tolower(c); });
        transform(q.begin(), q.end(), q.begin(), [](unsigned char c){ return tolower(c); });
        
        return p==q;
    }
};