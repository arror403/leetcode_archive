class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int m[26],n[26];
        for (int i=0;i<26;i++){
            m[i]=0;
            n[i]=0;
        }
        for (auto i:ransomNote) m[int(i)-97]++;
        for (auto i:magazine) n[int(i)-97]++;
        for (int i=0;i<26;i++){
            if (n[i]>=m[i]) continue;
            else return false;
        }

        return true;  
    }
};