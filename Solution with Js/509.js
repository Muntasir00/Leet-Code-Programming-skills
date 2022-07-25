var fib = function(n){
    function fib_seq(n){
        if(n===0) return n;
        if(n===1) return n;

        return fib_seq(n-1) + fib(n-2);
    }
    return fib_seq(n);
};

n = 10;
for (let i=0;i<=n;i++){
    console.log(fib(i))
}

