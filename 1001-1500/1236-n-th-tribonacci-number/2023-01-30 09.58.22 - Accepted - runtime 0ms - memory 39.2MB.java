class Solution {
    public int tribonacci(int n) {
        int []b = new int[41];
        b[0]=0;
        b[1]=1;
        b[2]=1;
        for (int i=3;i<=38;i++){
            b[i]=(b[i-1]+b[i-2]+b[i-3]);
        }
        return (b[n]);
     
    }
}