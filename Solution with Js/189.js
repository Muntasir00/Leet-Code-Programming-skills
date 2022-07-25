const revNums = (nums, start, end) => {
    while(start<end){
        [nums[start], nums[end]] = [nums[end], nums[start]];
        start++;
        end--;
    }
}

var rotate = function(nums, k){
    k = k%nums.length;
    nums.reverse();
    revNums(nums,0,k-1);
    revNums(nums,k,nums.length-1);
    return nums;
};
console.log(rotate([1,2,3,4,5,6,7],3))