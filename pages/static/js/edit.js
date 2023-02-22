function vald(){
  var id,mobilenumber;
  id=document.getElementById("id").value;
  mobilenumber=document.getElementById("mobile-number").value;
  if (isNaN(id)||isNaN(mobilenumber)){
    if(isNaN(id))
    {
      alert("id number must contain only numbers");
    }
  else if(isNaN(mobilenumber))
  {
    alert("mobile number must contain only numbers");
  }
  }
  if(id==" "||mobilenumber== " ")
  {
    if(id==" ")
    {
      alert(" id must not contain spaces");
    }
      if(mobilenumber==" ")
    {
      alert(" mobile number must not contain spaces");
    }
  }
}
function conf_del()
{
  confirm("do you want to delete ?");
}
function conf_edit()
{
  confirm("do you want to edit ?");
}