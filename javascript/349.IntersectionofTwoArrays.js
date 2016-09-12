/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    var nums=[];
    nums2.filter(function(elem, pos) {
        if(nums2.indexOf(elem) === pos&&nums1.indexOf(elem)!=-1 ){
            nums.push(nums2[pos]);
        }
    }); 

    return nums;
};
