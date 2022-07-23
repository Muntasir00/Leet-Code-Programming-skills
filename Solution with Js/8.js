var myAtoi = function(s){
    let i = 0;
    let result = 0;
    let isNeg = false;
    while(s[i]==' '){
        i++;
    }
    if(s[i]==='+'|| s[i]==='-'){
        isNeg = s[i] === '-';
        i++;
    }
    for(i;i<s.length;i++){
        const currentValue = s.charCodeAt(i) - 48;
        if(currentValue<0 || currentValue > 9){
            break;
        }
        result*=10;
        result+=currentValue;
    }
    if(isNeg){
        result=-result;
    }
    return result;

}

console.log(myAtoi("42"))