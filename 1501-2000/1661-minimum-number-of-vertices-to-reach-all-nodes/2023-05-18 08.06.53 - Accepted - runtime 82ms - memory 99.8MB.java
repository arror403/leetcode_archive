class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Map<Integer, Integer> indeg = new HashMap<>();

        for (List<Integer> edge : edges) {
            int u = edge.get(0);
            int v = edge.get(1);
            graph.computeIfAbsent(u, key -> new ArrayList<>()).add(v);
            indeg.put(v, indeg.getOrDefault(v, 0) + 1);
        }

        List<Integer> ans = new ArrayList<>();
        for (Map.Entry<Integer, List<Integer>> entry : graph.entrySet()) {
            int u = entry.getKey();
            if (!indeg.containsKey(u) || indeg.get(u) == 0) {
                ans.add(u);
            }
        }

        return ans;
    }
}