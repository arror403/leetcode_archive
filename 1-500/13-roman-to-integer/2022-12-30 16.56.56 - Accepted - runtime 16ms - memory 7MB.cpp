class Solution {
public:
    int romanToInt(string s) {
        vector <int> b;
        int sum=0;
        for (int i=0;i<s.length();i++){
            if (s[i]=='I')
                b.push_back(1);
            else if (s[i]=='V')
                b.push_back(5);
            else if (s[i]=='X')
                b.push_back(10);
            else if (s[i]=='L')
                b.push_back(50);
            else if (s[i]=='C')
                b.push_back(100);
            else if (s[i]=='D')
                b.push_back(500);
            else if (s[i]=='M')
                b.push_back(1000);
        }

        for (int j=0;j<b.size()-1;j++){
            if (b[j]<b[j+1])
                sum-=b[j];
            else
                sum+=b[j];
        }
        sum+=b[b.size()-1];
        return sum;
    }
};