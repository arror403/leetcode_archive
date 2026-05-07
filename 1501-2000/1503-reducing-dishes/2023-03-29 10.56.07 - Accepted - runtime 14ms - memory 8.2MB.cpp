class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        vector<int> b;
        int index,sum,m;
        sort(satisfaction.begin(),satisfaction.end());
        for (int n=0;n<satisfaction.size();n++){
            index=1;
            sum=0;
            
            for (auto i :satisfaction){
                sum+=index*i;
                index+=1;
            }
            b.push_back(sum);

            auto minIt = min_element(satisfaction.begin(), satisfaction.end()); // Find the minimum element

            satisfaction.erase(minIt); // Remove the minimum element
        }
        m=*max_element(b.begin(),b.end());
        if (m<0) return 0;
        else return m;       
    }
};

        // b=[]
        // satisfaction.sort()
        // for n in range(0,len(satisfaction)):
        //     index=1
        //     sum=0
            
        //     for i in satisfaction:
        //         sum+=index*i
        //         index+=1
            
        //     b.append(sum)
            
        //     satisfaction.remove(min(satisfaction))
        //     # print(satisfaction)
        // if max(b)<0: return 0
        // else : return max(b)