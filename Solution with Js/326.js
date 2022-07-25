// var isPowerThree = function(n){
//     // console.log(Math.log10(n)/Math.log10(3))
//     return (Math.log10(n)/Math.log10(3))%1 ==0;

// };

// console.log(isPowerThree(26))
var isPowerThree = function(n){
    if(n<1){
        return false;
    }
    while(n%3===0){
        n=n/3;
    }
    return n===1;
}