 Create Account
 <!--
 <html>
   <label for="Create-Username>">Create-Username</label>
   <br><input type="text" id="Create-Username" name="CreateUsername" placeholder="MatiD1234">
  <br><input type="text" id="Create-Password" name="Create-Password" placeholder="1234">
  <br>
  <a href="https://hsinaditam.github.io/Password_Man/CreateAccount.html">
     <input class="submit" type="submit" value="Create Account">
   <a href="https://hsinaditam.github.io/Password_Man/HomePage.html">
     <input class="submit" type="submit" value='Log In'>
 -->

 <form action="create_User()">
     <p><label>
         Name:
         <input type="text" name="name" id="name" required>
     </label></p>
     <p><label>
         User ID:
         <input type="text" name="uid" id="uid" required>
     </label></p>
     <p><label>
         Password:
         <input type="password" name="password" id="password" required>
         Verify Password:
         <input type="password" name="passwordV" id="passwordV" required>
     </label></p>
     <p><label>
         Phone:
         <input type="tel" name="phone_num" id="phone_num"
             pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
             placeholder="999-999-9999">
     </label></p>
     <p><label>
         Birthday:
         <input type="date" name="dob" id="dob">
     </label></p>
     <p>
         <button class="submit">Create</button>
     </p>
 </form>