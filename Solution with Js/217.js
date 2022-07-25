function containDuplicate(nums){
    nums.sort((a,b) => {return b-a});
    console.log(nums);
    for (let i=0;i<nums.length;i++){
        if(i>0 && nums[i-1]=== nums[i]) {
            console.log(nums[i])
            return true;}
    }
    return false
}; 
// function containDuplicate(nums){

// }
console.log(containDuplicate([1,2,3,1,5,6,7,8,2,2]))