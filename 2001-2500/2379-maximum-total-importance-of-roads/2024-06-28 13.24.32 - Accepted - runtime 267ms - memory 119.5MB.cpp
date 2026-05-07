class Solution {
public:
    //##### improved by Claude #####
    
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        vector<int> degree(n, 0);
        long long result = 0;

        // Count the degree of each node
        for (const auto& road : roads) {
            ++degree[road[0]];
            ++degree[road[1]];
        }

        // Sort the degrees in descending order
        sort(degree.rbegin(), degree.rend());

        // Calculate the maximum importance
        for (int i = 0; i < n; ++i) {
            result += static_cast<long long>(degree[i]) * (n - i);
        }

        return result;
    }
};