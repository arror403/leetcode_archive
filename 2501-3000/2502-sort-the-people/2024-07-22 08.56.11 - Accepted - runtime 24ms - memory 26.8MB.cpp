class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<pair<int,string>> p;

        for (size_t i=0; i<names.size(); ++i)
            p.emplace_back(heights[i], names[i]);

        sort(p.begin(), p.end(), greater<>());

        vector<string> res;
        
        for (const auto& x : p)
            res.push_back(x.second);

        return res;
    }

};