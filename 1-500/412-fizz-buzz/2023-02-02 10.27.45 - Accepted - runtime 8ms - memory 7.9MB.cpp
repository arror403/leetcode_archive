class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> b;
        for (int i=1;i<=n;i++){
            if (i%3==0 and i%5==0)
                b.push_back("FizzBuzz");
            else if (i%3==0)
                b.push_back("Fizz");
            else if (i%5==0)
                b.push_back("Buzz");
            else
                b.push_back(to_string(i));
        }
        return b;
    }
};