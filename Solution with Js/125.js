var isPalindrome = function(s){
    console.log(s)
    s = s.replace(/[^a-zA-Z0-9]/g,'')
    console.log(s)
    for (let [i,j]=[,s.length-1];i<j;){
        if(s[i]!=s[j]){
            return false
        }
        i++
        j--
    }
    return true
}
let s = "A man, a plan, a canal: Panama"
console.log(isPalindrome(s))

