var i =1;
function showname(){
    if(i==1){
        document.getElementById("showname").style.transitionProperty="width";
        document.getElementById("showname").style.width="500px";
        document.getElementById("showname").style.transitionDuration="2s";
        document.getElementById("showname").style.transitionTimingFunction="linear";
        return i=0;
    }
    else{
        document.getElementById("showname").style.transitionProperty="width";
        document.getElementById("showname").style.width="0px";
        document.getElementById("showname").style.transitionDuration="2s";
        document.getElementById("showname").style.transitionTimingFunction="linear";
        return i=1;
    }
}