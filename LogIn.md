## About This Project
This is a project that we will develop in the coming weeks. Firstly we changed and tweaked the css and sass to our liking. in the next few weeks, we will add a log-in screen and a databases to store all of your passwords in a secure, encrypted place.

## Log-in
<form>
  <label for="Username>">Username</label>
  <br><input type="text" id="Login-Username" name="user-login" placeholder="MatiD">
  <br><br><label for="Password" id="Login-Password" name="user-password" >Password</label>
  <br><input type="text" id="Login-Password" name="Password" placeholder="PleaseStealMyCreditCard">
  <br>
  <br>
  <a href=http://localhost:4001/CreateAccount.html>
    <input class="submit" type="submit" value="Create Account">
    
  <a href=http://localhost:4001/HomePage.html>
    <input class="submit" type="submit" value='Log In'>

<style>
    input[type=text], input[type=password]{
      font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", 
      Helvetica, Arial, "Lucida Grande", sans-serif;
      border-radius: 0.5em;
      box-shadow: 0.75em;
      min-width: 150px;
      padding: 5px 5px;


    }
    
    .submit{
        list-style-type: none;
        width: 132px;
        min-height: 40px;
        margin-bottom: 12px;
        line-height: 1em;
        padding: 6px 6px 6px 7px;
        background: #AF0011;
        background: -moz-linear-gradient(top, #AF0011 0%, #820011 100%);
        background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #f8f8f8), color-stop(100%, #dddddd));
        background: -webkit-linear-gradient(top, #AF0011 0%, #820011 100%);
        background: -o-linear-gradient(top, #AF0011 0%, #820011 100%);
        background: -ms-linear-gradient(top, #AF0011 0%, #820011 100%);
        background: linear-gradient(to top, #AF0011 0%, #820011 100%);
        border-radius: 0.75em;
        border: 1px solid #0D0D0D;
        -webkit-box-shadow: inset 0px 1px 1px 0 #e90226;
        box-shadow: inset 0px 1px 1px 0 #e90226;
        color: white;

        }
</style>