function login()
	{
		var username = document.getElementById("in1").value;
		var password = document.getElementById("in2").value;
		var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		if(username =='')
		{
			alert("Please enter your username");
		}
		else if(password=='')
		{
        	alert("Please enter your password");
		}
		else if(password.length < 8)
		{
			alert("Password length must be not less than 8 characters");
		}
		else
		{
		//alert('Successful log in');
    	// window.location = "../pages/home.html";
		// window.location.href( "../pages/home.html") ;
		document.getElementById("form").action = "../pages/home.html";
		}
    }
	