class Solution {
public:
    vector<int> countBits(int n) {
       vector<int> b;
       for (int i=0;i<=n;i++) b.push_back(0);
        
        // for i in range(1, num + 1):
        for (int i=1;i<=n;i++)
            // Using Brian Kernighan's algorithm to count set bits
            b[i] = b[i & (i - 1)] + 1;
        
        return b; 
    }
};