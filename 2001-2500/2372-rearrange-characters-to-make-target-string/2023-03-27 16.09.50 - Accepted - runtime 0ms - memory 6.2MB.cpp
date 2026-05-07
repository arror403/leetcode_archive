class Solution {
public:
    int rearrangeCharacters(string s, string target) {
        int a[26]={0};
        int b[26]={0};
        vector<int> m;
        for (auto i : s) a[char(i)-97]+=1;
        for (auto i : target) b[char(i)-97]+=1;
        for (int i=0;i<26;i++){
            if (b[i]==0) continue;
            else m.push_back(int(a[i]/b[i]));
        }
        return *min_element(m.begin(),m.end());        
    }
};