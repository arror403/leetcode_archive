class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        vector<vector<int>> b;
        vector<int> t;
        int d=INT_MAX,tmp;
        for (int i=0;i<arr.size()-1;i++){
            tmp=abs(arr[i]-arr[i+1]);
            if (tmp<d) d=tmp;
        }
        cout << d;
        for (int i=0;i<arr.size()-1;i++){
            t.clear();
            tmp=abs(arr[i]-arr[i+1]);
            if (tmp==d){
                t.push_back(arr[i]);
                t.push_back(arr[i+1]);
                b.push_back(t);
            }
        }
        return b;
    }
};

        // arr.sort()
        // b=[]
        // d = float('inf')
        // for i in range(len(arr)-1):
        //     if abs(arr[i]-arr[i+1])<d:
        //         d=abs(arr[i]-arr[i+1])
            
        // for i in range(len(arr)-1):
        //     if abs(arr[i]-arr[i+1])==d:
        //         tmp=[arr[i],arr[i+1]]
        //         b.append(tmp)
                
        // return b