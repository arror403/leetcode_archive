class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        char *cstr1 = new char[text1.length() + 1];
        strcpy(cstr1, text1.c_str());
        char *cstr2 = new char[text2.length() + 1];
        strcpy(cstr2, text2.c_str());       
        return lcs(cstr1,cstr2,strlen(cstr1),strlen(cstr2));
    }
    /* Returns length of LCS for X[0..m-1], Y[0..n-1] */
    int lcs(char *X, char *Y, int m, int n){
        // initializing a matrix of size (m+1)*(n+1)
        int L[m + 1][n + 1];
    
        /* Following steps build L[m+1][n+1] in bottom up fashion. Note
            that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] */
        for (int i = 0; i <= m; i++)
        {
            for (int j = 0; j <= n; j++)
            {
                if (i == 0 || j == 0)
                    L[i][j] = 0;
    
                else if (X[i - 1] == Y[j - 1])
                    L[i][j] = L[i - 1][j - 1] + 1;
    
                else
                    L[i][j] = max(L[i - 1][j], L[i][j - 1]);
            }
        }
    
        // L[m][n] contains length of LCS for X[0..n-1] and Y[0..m-1]
        return L[m][n];
    }
};


        
        
        
        
