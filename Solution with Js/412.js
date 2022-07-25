var fizzBuzz = function(n){
    let output = [];
    for (let i=1;i<=n;i++){
        console.log(i)
        if(i%3===0 && i%5===0){
            output.push('FizzBuzz');
        }else if(i%3==0){
            output.push('fizz');
        }else if(i%5==0){
            output.push('Buzz');
        }
        else {
            output.push(i.toString());
        }

        
    }
    return output
}

console.log(fizzBuzz(15))