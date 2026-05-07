class Solution {
public:
    int percentageLetter(string s, char letter) {
        int n=s.length();
        int count=0;
        for(char x: s){
            if(x==letter){
                count++;
            }
        }
        return count*100/n;
    }
        // float a=0.0;
        // int b=s.length();
        // for (int i=0;i<b;i++){
        //     if (s[i]==letter) a+=1.0;
        // }
        // return a/float(b)*100.0;
};