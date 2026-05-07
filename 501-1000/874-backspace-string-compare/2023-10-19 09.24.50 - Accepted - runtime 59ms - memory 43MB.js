/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    function buildString(str) {
        const result = [];
        for (const char of str) {
            if (char !== '#') {
                result.push(char);
            } 
            else if (result.length > 0) {
                result.pop();
            }
        }
        return result.join('');
    }
    
    return buildString(s) === buildString(t);
};