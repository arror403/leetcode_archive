class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        // Create adjacency list
        vector<vector<pair<int, double>>> graph(n);
        for (int i = 0; i < edges.size(); i++) {
            int a = edges[i][0], b = edges[i][1];
            double p = succProb[i];
            graph[a].push_back({b, p});
            graph[b].push_back({a, p});
        }
        
        vector<double> probabilities(n, 0.0);
        probabilities[start] = 1.0;
        
        // Priority queue for Dijkstra's algorithm
        priority_queue<pair<double, int>> pq;
        pq.push({1.0, start});
        
        while (!pq.empty()) {
            double prob = pq.top().first;
            int node = pq.top().second;
            pq.pop();
            
            if (node == end) return prob;
            
            if (prob < probabilities[node]) continue;
            
            for (const auto& [neighbor, edge_prob] : graph[node]) {
                double new_prob = prob * edge_prob;
                if (new_prob > probabilities[neighbor]) {
                    probabilities[neighbor] = new_prob;
                    pq.push({new_prob, neighbor});
                }
            }
        }
        
        return 0.0;        
    }
};