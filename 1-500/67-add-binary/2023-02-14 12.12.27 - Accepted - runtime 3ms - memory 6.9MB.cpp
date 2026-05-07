class Solution {
public:
    string addBinary(string str1, string str2) {
    string sum="";
    int len1, len2, i, j, ds=0;
    len1 = str1.size();
    len2 = str2.size();
    i = len1 - 1;
    j = len2 - 1;
    while(i>=0 || j>=0 || ds==1) {
        ds = ds + ((i >= 0) ? str1[i] - '0' : 0);
        ds = ds + ((j >= 0) ? str2[j] - '0' : 0);
        sum = char(ds % 2 + '0') + sum;
        ds = ds/2;
        i--;
        j--;
    }
    return sum;
    }
};

