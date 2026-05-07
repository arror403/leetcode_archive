class Solution {
public:
    int countTriples(int n) {
        int t=0;
        double s;
        for (int i=1;i<n;i++){
            for (int j=i+1;j<n+1;j++){
                s=pow((i*i+j*j),(0.5));
                if (int(s)==s && s<=n) t+=2;
            }
        }
        return t;
    }
};

        // t=0
        // for i in range(1,n):
        //     for j in range(i+1,n+1):
        //         s=(i*i+j*j)**(0.5)
        //         if int(s)==s and s<=n:
        //             t+=2
        // return t