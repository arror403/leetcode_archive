class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        unordered_map<int, vector<int>> graph;
        unordered_map<int, int> indeg;

        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            graph[u].push_back(v);
            indeg[v]++;
        }

        vector<int> ans;
        for (auto& entry : graph) {
            int u = entry.first;
            if (indeg[u] == 0) {
                ans.push_back(u);
            }
        }

        return ans;
    }
};