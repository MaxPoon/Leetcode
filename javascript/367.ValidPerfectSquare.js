/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    if(num === 1 || num === 0) return true;
    else{
        var i = 2;
        while(true){
            var x=i*i;
            if ( x=== num) return true;
            else if(x>num) return false;
            i++;
        }
    }
};
