
 var  count = (function(){
    
    var counter = 0;
    
    return function() {return counter++}
    })()
    
    function displaycount(){
    document.getElementById("carrier").innerHTML = count();
    }
