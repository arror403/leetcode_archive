class Solution {
public:
    int addDigits(int num) {
        while(num>=10){
            num=sum(intToVector(num));
        }
        return num;
    }

    vector<int> intToVector(int num) {
        vector<int> digits;
        while (num > 0) {
            digits.push_back(num % 10);
            num /= 10;
        }
        reverse(digits.begin(), digits.end()); // Reverse the order of digits
        return digits;
    }


    int sum(vector<int> vec) {
        int total = 0;
        for (int i = 0; i < vec.size(); i++) {
            total += vec[i];
        }
        return total;
    }    
    
};