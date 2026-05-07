/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
        const b = [0, 1, 1];
        for (let i = 3; i <= 38; i++) {
            b.push(b[i - 1] + b[i - 2] + b[i - 3]);
        }
        return b[n];  
};