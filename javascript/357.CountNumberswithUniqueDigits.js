/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    if (n===0) return 1;
    if (n===1) return 10;
    if (n===2) return 91;
    if(n===3) return 739;
    else{
        var sum = 0;
        for(var i=1;i<=n;i++){
            sum+=f(i);
        }
        return sum;
    }
    function f(k){
        if(k===1) return 10;
        if (k===2) return 81;
        if (k===3) return 648;
        else{
            var result = 9;
            for(var i=9;i>=9-k+2;i--){
                result*=i;
            }
            return result;
        }
    }
};
