/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    var index=[];
    var vowels=[];
    var result="";
    for(var i=0;i<s.length;i++){
        var c=s.charAt(i);
        if (c==='a'||c==='e'||c==='i'||c==='o'||c==='u'||c==='A'||c==='E'||c==='I'||c==='O'||c==='U'){
            index.push(i);
            vowels.push(c);
        }
    }
    for(i=0;i<s.length;i++){
        c=s.charAt(i);
        if (c==='a'||c==='e'||c==='i'||c==='o'||c==='u'||c==='A'||c==='E'||c==='I'||c==='O'||c==='U'){
            result+=vowels[vowels.length-1];
            vowels.pop();
        }else{
            result+=c;
        }
    }
    return result;
};
