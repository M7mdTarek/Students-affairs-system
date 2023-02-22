var i =1;
function showname(){
    if(i==1){
        document.getElementById("addshow").style.backgroundColor="#7367f0";
        document.getElementById("addlist_show").style.display="block";
        document.getElementById("addlist_show").style.height="fit-content";
       
        
        document.getElementById("addshow").style.transitionDuration="0.8s";
        

        return i=0;
    }
    else{
        document.getElementById("addshow").style.backgroundColor="whitesmoke";
        document.getElementById("addlist_show").style.display="none";
        document.getElementById("addlist_show").style.height="0px";
       
        document.getElementById("addshow").style.transitionDuration="0.8s";
       
        return i=1;
    }
}
var x =1;
function show2(){
    if(x==1){
        document.getElementById("editshow").style.backgroundColor="#7367f0";
        document.getElementById("editlist_show").style.display="block";
        document.getElementById("editlist_show").style.height="fit-content";
       
        
        document.getElementById("editshow").style.transitionDuration="0.8s";
        

        return x=0;
    }
    else{
        document.getElementById("editshow").style.backgroundColor="whitesmoke";
        document.getElementById("editlist_show").style.display="none";
        document.getElementById("editlist_show").style.height="0px";
       
        document.getElementById("editshow").style.transitionDuration="0.8s";
       
        return x=1;
    }
}
var y =1;
function show3(){
    if(y==1){
        document.getElementById("deleteshow").style.backgroundColor="#7367f0";
        document.getElementById("deleteshow_list").style.display="block";
        document.getElementById("deleteshow_list").style.height="fit-content";
       
        
        document.getElementById("deleteshow").style.transitionDuration="0.8s";
        

        return y=0;
    }
    else{
        document.getElementById("deleteshow").style.backgroundColor="whitesmoke";
        document.getElementById("deleteshow_list").style.display="none";
        document.getElementById("deleteshow_list").style.height="0px";
       
        document.getElementById("deleteshow").style.transitionDuration="0.8s";
       
        return y=1;
    }
}

var z =1;
function show4(){
    if(z==1){
        document.getElementById("assginshow").style.backgroundColor="#7367f0";
        document.getElementById("assginshow_lists").style.display="block";
        document.getElementById("assginshow_lists").style.height="fit-content";
        document.getElementById("assginshow").style.transitionDuration="0.8s";
        

        return z=0;
    }
    else{
        document.getElementById("assginshow").style.backgroundColor="whitesmoke";
        document.getElementById("assginshow_lists").style.display="none";
        document.getElementById("assginshow_lists").style.height="0px";
       
        document.getElementById("assginshow").style.transitionDuration="0.8s";
       
        return z=1;
    }
}



