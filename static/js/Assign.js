function Assign(){
    var name, id, filter;
    name = document.getElementById("1").value;
    id = document.getElementById("2").value;
    filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (name == '' || id == ''){
        alert("Please enter all the information!");
    }
    else if(id < 0 || id == 0)
    {
        alert("Please Enter a valid ID");
    }
}