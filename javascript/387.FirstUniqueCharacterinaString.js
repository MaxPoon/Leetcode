/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    var count={};
    for(var i=0;i<s.length;i++){
        if(count[s.charAt(i)]) count[s.charAt(i)] = count[s.charAt(i)]+1;
        else count[s.charAt(i)]=1;
    }
    for(var i=0;i<s.length;i++){
        if(count[s.charAt(i)]===1) return i;
    }
    return -1;
};
