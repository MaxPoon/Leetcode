/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {
    if (n<1) return false;
    var x=Math.round(Math.log(n)/Math.log(3));
    if(Math.pow(3,x)===n) return true;
    else return false;
};
