var reverse = function(x){
    let revNum = 0, lastnum=0;
    while(x!=0){
        lastnum = x%10;
        x = parseInt(x/10);
        revNum = revNum*10+lastnum;
        if(x<Math.pow(-2,31)||x>Math.pow(2,31)-1) return 0;
    }
 
    return revNum;
}
y = reverse(123)
console.log(y)