/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if(n<1) return false;
    return Boolean((n&(n-1))===0);
};
