class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> b;
        int sum,i,n;

        for (int i=0;i<num+1;i++){
            sum=0;
            n=i;
            while(n!=0){
                if (n%2==1){
                    sum+=1;
                    n/=2;
                }
                else if (n%2==0){
                    n/=2;
                }
            }
            b.push_back(sum);
        }
        return b;
    }
};
    // def countBits(self, num: int) -> List[int]:
    //     b=[]
    //     for i in range(0,num+1):
    //         sum=0
    //         n=i
    //         while n!=0:
    //             if n%2==1:
    //                 sum+=1
    //                 n=int(n/2)
    //             elif n%2==0:
    //                 n=int(n/2)
    //         b.append(sum)
            
    //     return b