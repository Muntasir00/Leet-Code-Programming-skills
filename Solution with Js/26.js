var removeDuplicates = function (nums) {
    const numsLength = nums.length;
  
    if (numsLength === 0) {
      return 0;
    }
  
    let j = 1;
    for (let i = 0; i < numsLength - 1; i++) {
      if (nums[i] !== nums[i + 1]) {
        nums[j] = nums[i + 1];
        j++;
      }
    }
  
    return j;
  };

console.log(removeDuplicates([1,1,2]))