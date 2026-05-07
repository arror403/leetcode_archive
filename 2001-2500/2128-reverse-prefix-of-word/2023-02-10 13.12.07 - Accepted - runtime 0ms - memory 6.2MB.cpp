class Solution {
public:
    string reversePrefix(string word, char ch) {
        string res="";
        int x=0;
        for (int i=0;i<word.length();i++){
            if (word[i]==ch){
                x=i;
                break;
            }
        }
        for (int i=0;i<(x+1);i++) res+=word[i];
        reverse(res.begin(), res.end());
        for (int i=x+1;i<word.length();i++) res+=word[i];
        return res;
    }
};

        // res=""
        // x=0
        // for i in range(len(word)):
        //     if word[i]==ch:
        //         x=i
        //         break

        // for i in range(x+1): res+=word[i]
        // # print(res)

        // res=res[::-1]
    
        // for i in range(x+1,len(word)): res+=word[i]

        // return res