/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    var nums = [];
    for(var i=0;i<nums1.length;i++){
        var element = nums1[i];
        n=nums2.indexOf(element);
        if (n>=0){
            nums.push(element);
            nums1.splice(i, 1);
            nums2.splice(n,1);
            i--;
        }
    }
    return nums;
};
