var reverseString = function(s){
    let first = 0;
    let last =s.length - 1 ;
    while(first<last){
        temp = s[first];
        s[first] = s[last];
        s[last] = temp;
        first++ ;
        last-- ;

    }
    return s;

}
var y = reverseString(["h","e","l","l","o"])
console.log(y)