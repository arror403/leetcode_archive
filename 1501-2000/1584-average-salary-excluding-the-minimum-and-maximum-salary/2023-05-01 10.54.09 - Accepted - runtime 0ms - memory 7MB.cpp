class Solution {
public:
    double average(std::vector<int>& salary) {
        std::sort(salary.begin(), salary.end());
        salary.erase(salary.begin());
        salary.erase(salary.end()-1);
        
        return static_cast<double>(std::accumulate(salary.begin(), salary.end(), 0)) / salary.size();
    }
};