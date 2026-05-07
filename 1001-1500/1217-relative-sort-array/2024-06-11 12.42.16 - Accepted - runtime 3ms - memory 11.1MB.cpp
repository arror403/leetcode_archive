class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
    unordered_map<int, int> p;
    vector<int> a, b;

    for (int i = 0; i < arr2.size(); ++i) p[arr2[i]] = i;
    
    for (int x : arr1) {
        if (p.find(x) != p.end())
            b.push_back(x);
        else
            a.push_back(x);
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end(), [&p](int x, int y) {return p[x] < p[y];});

    vector<int> res = b;
    res.insert(res.end(), a.begin(), a.end());


    return res;

    }
};