var isAnargram = function(s, t){
    if(s.length===t.length){
        sarray=s.split("")
        tarrray=t.split("")
        sarray.sort()
        tarrray.sort()
        for(i=0;i<s.length;i++){
            if(sarray[i]!==tarrray[i]){
                return false
            }
        }
        return true
    }else{
        return false;
    }
}

let s = "anagram";
let t = "nagaram";
console.log(isAnargram(s,t))