class Solution {
public:
    bool checkAlmostEquivalent(string word1, string word2) {
        vector<int> a,b;
        bool f=true;
        for (int i=0;i<26;i++){
            a.push_back(0);
            b.push_back(0);
        }
        for (auto i:word1) a[int(i)-97]++;
        for (auto i:word2) b[int(i)-97]++;
        for (int i=0;i<26;i++){
            if (abs(a[i]-b[i])>3){
                f=false;
                break;
            }
        }
        return f;
    }
};
        // a,b,f=[0]*26,[0]*26,True
        // for i in word1: a[ord(i)-97]+=1
        // for i in word2: b[ord(i)-97]+=1
            
        // for i in range(26):
        //     if abs(a[i]-b[i])>3:
        //         f=False
        //         break
                
        // return f