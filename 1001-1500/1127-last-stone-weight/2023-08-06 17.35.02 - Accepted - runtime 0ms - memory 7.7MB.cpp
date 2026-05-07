#include <vector>
#include <queue>
#include <functional>

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap;  // Use max heap (default in C++)
        for (int stone : stones) {
            maxHeap.push(stone);  // Push stones into the max heap
        }

        while (maxHeap.size() > 1) {
            int x = maxHeap.top();  // Get the two largest stones
            maxHeap.pop();
            int y = maxHeap.top();
            maxHeap.pop();

            if (x != y) {
                maxHeap.push(x - y);  // Add the difference back to the max heap
            }
        }

        return maxHeap.empty() ? 0 : maxHeap.top();  // Return the last stone weight or 0 if the heap is empty
    }
};