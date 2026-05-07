class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        unordered_map<int, int> t;
        vector<long long> f;
        long long res=0;
        for(auto e: roads){
            t[e[0]]++;
            t[e[1]]++;
        }
        for(auto p: t) f.push_back(p.second);
        sort(f.begin(), f.end());
        reverse(f.begin(), f.end());
        for(long long v: f){
            res+=v*n;
            n--;
        }
        return res;
    }
};

// t=sorted(Counter(chain.from_iterable(roads)).values(), reverse=1)
// return sum(t[i]*(n-i) for i in range(len(t)))