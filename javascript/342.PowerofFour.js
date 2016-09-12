/**
 * @param {number} num
 * @return {boolean}
 */
var isPowerOfFour = function(num) {
 return num > 0 && (num & (num - 1)) ==0  && (num & 0x55555555) !=0;
};
