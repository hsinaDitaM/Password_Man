## About This Project
This is a project that we will develop in the coming weeks. Firstly we changed and tweaked the css and sass to our liking. in the next few weeks, we will add a log-in screen and a databases to store all of your passwords in a secure, encrypted place.

## Log-in
<form>
<!---<form action="/action_page.php">-->
  <label class = "text" for="fname">Username</label>
  <br/>
  <input class = "text" type="text" id="fname" name="fname"><br><br>
  <label for="lname">Password</label>
  <br/>
  <input class = "text" type="text" id="lname" name="lname"><br><br>
  <input class ="submit" type="submit" value="Submit">
<input class ="submit" type="submit" value="Create Account">
</form>
<style>
    .submit{
        list-style-type: none;
        width: 132px;
        height: 30px;
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
        border-radius: 4px;
        border: 1px solid #0D0D0D;
        -webkit-box-shadow: inset 0px 1px 1px 0 #e90226;
        box-shadow: inset 0px 1px 1px 0 #e90226;
        color: white;
        }
</style>