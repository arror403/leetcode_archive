class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        int tmp,a,b;
        for(int i=0;i<edges.size();i++){
            if (edges[i][0]>edges[i][1]){
                tmp=edges[i][0];
                edges[i][0]=edges[i][1];
                edges[i][1]=tmp;
            }
        }
        a=edges[0][0];
        b=edges[0][1];
        if (a == edges[1][0]) return a;
        else return b;
    }
};

        // for i in range(len(edges)):
        //     if edges[i][0]>edges[i][1]:
        //         tmp=edges[i][0]
        //         edges[i][0]=edges[i][1]
        //         edges[i][1]=tmp
                
                
        // a=edges[0][0]
        // b=edges[0][1]       
        
        // if a == edges[1][0]:
        //     return a
        // else:
        //     return b