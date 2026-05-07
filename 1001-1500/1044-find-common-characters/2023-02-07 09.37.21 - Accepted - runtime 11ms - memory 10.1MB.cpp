class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<vector<int>> w;
        vector<string> res;
        vector<int> tmp,x;
        int l,p;
        
        for (auto i: words){
            tmp.clear();
            for (int i=0;i<26;i++) tmp.push_back(0);
            for (auto j: i) tmp[int(j)-97]++;
            w.push_back(tmp);
        }
        
        for (int j=0;j<26;j++){
            x.clear();
            for (int i=0;i<w.size();i++) x.push_back(w[i][j]);
            l=*min_element(x.begin(), x.end());
            for(int k=0;k<l;k++){
                string s1; 
                s1=(char) (97+j);
                res.push_back(s1);
            }
        }
        return res;
    }
};