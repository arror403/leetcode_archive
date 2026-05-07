class Solution {
public:
    std::vector<std::string> sortPeople(std::vector<std::string>& names, std::vector<int>& heights) {
        std::vector<std::vector<int>> t;
        std::vector<std::string> res;
        for (int i = 0; i < names.size(); i++) {
            std::vector<int> tmp = {i, heights[i]};
            t.push_back(tmp);
        }
        std::sort(t.begin(), t.end(), [](std::vector<int>& a, std::vector<int>& b) {return a[1] > b[1];});
        for (auto i : t) {
            res.push_back(names[i[0]]);
        }
        return res;
    }
};