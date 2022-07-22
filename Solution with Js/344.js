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

}
console.log(reverseString(["H","a","n","n","a","h"]))