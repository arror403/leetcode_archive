class Solution {
public:
    int removeDuplicates(vector<int>& A) {
        int count = 0;
        for (int i=1;i<A.size();i++){
            if (A[i] == A[i-1]) count++;
            else A[i-count] = A[i];
        }
        return A.size()-count;
    }
};

    // def removeDuplicates(self, A: List[int]) -> int:
    //     count = 0
    //     for i in range(1,len(A)):
    //         if (A[i] == A[i-1]):
    //             count+=1
    //         else:
    //             A[i-count] = A[i]
    //     return len(A)-count