function ordArray(x){
    var a = [];
    for(var i=0;i<x.length;i++){
        a.push(ord(x[i]));
    }
    return a;
}
function chrArray(x){
    var a = [];
    for(var i=0;i<x.length;i++){
        a.push(chr(x[i]));
    }
    return a;
}