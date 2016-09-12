/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var result =0;
    var negative=false;
    if(x<0) {
        negative=true;
        x=-x;
    }
    while(x>0){
        var temp=x%10;
        result=result*10+temp;
        if(result>2147483642) return 0;
        x=Math.floor(x/10);
    }
    if(negative) result=-result;
    return result;
};
