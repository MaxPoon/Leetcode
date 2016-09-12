/**
 * @param {number} num
 * @return {number[]}
 */
var countBits = function(num) {
    var result = [];
    for (var i=0;i<=num;i++){
        if (i===0) result.push(0);
        else{
            x=i-Math.pow(2,Math.floor(Math.log2(i)));
            result.push(result[x]+1);
        }
    }
    return result;
};
