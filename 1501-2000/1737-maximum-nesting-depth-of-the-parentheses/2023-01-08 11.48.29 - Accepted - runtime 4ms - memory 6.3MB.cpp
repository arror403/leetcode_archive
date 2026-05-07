class Solution {
public:
    int maxDepth(string s) {
        int n=0;
        vector<int> b={0};
        for (int i=0;i<s.length();i++){
            if (s[i]=='('){
                n++;
                b.push_back(n);
            }
            else if (s[i]==')'){
                n--;
                b.push_back(n);
            }
        }
        return int(*max_element(b.begin(), b.end()));
    }
};


        // n=0
        // b=[0]
        // for i in s:
        //     if i=='(':
        //         n+=1
        //         b.append(n)
        //     elif i==')':
        //         n-=1
        //         b.append(n)
        // return (max(b))