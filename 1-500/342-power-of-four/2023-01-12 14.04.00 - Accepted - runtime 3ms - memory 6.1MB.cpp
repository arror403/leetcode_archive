class Solution {
public:
    bool isPowerOfFour(int n) {
        vector<int> b={1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824};
        for (int i=0;i<b.size();i++) if (b[i]==n) return true;
        return false;
    }
};