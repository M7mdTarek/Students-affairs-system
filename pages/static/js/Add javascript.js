function add(){
    var name, id, dateOfBirth, GPA, department, email, mobile, filter;
    name = document.getElementById("1").value;
    id = document.getElementById("2").value;
    dateOfBirth = document.getElementById("3").value;
    GPA = document.getElementById("4").value;
    department = document.getElementById("8").value;
    email = document.getElementById("9").value;
    mobile = document.getElementById("10").value;
    filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (name == '' || id == '' || dateOfBirth == '' || GPA == '' || department == '' || email == '' || mobile ==''){
        alert("Please enter all the information!")
    }
    else if (!filter.test(email)){
        alert("Email is not correct please enter a valid email");
    }
    else if (mobile.length != 11){
        alert("The mobile number must be 11 numbers")
    }
}