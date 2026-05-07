class Solution {
public:
    int percentageLetter(string s, char letter) {
        int a=0;
        int b=s.length();
        for (char x:s){
            if (x==letter) a++;
        }
        return a*100/b;
    }
};