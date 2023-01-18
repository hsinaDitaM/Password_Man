

<a class="submit" href="https://hsinaditam.github.io/Password_Man/">Log out</a>

### Passwords
<table>
    <tr>
        <th><label for="name">Name</label></th>
        <th><label for="email">Email</label></th>
        <th><label for="password">Password</label></th>
        <th><label for="phone">Phone</label></th>
    </tr>
    <tr>
        <td><input type="text" name="name" id="name" placeholder="Mati" required></td>
        <td><input type="email" name="email" id="email" placeholder="MatiMakesBank@yahoo.com" required></td>
        <td><input type="password" name="password" id="password" placeholder="Password123" required></td>
        <td><input type="tel" name="phone_num" id="phone_num"
            pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
            placeholder="999-999-9999"></td>
        <td ><button onclick="create_User()">Create</button></td>
    </tr>
</table>


### Credit Card info



### Calender & reminders
<style>

      * {box-sizing: border-box;}
      ul {list-style-type: none;}
      body {font-family: Verdana, sans-serif;}

      .month {
        padding: 70px 25px;
        width: 100%;
        background: #010302;
        text-align: center;
      }

      .month ul {
        margin: 0;
        padding: 0;
      }

      .month ul li {
        color: white;
        font-size: 20px;
        text-transform: uppercase;
        letter-spacing: 3px;
      }

      .month .prev {
        float: left;
        padding-top: 10px;
      }

      .month .next {
        float: right;
        padding-top: 10px;
      }

      .weekdays {
        margin: 0;
        padding: 10px 0;
        background-color: #ddd;
      }

      .weekdays li {
        display: inline-block;
        width: 13.6%;
        color: #666;
        text-align: center;
      }

      .days {
        padding: 10px 0;
        background: #eee;
        margin: 0;
      }

      .days li {
        list-style-type: none;
        display: inline-block;
        width: 13.6%;
        text-align: center;
        margin-bottom: 5px;
        font-size:12px;
        color: #777;
      }

      .days li .active {
        padding: 5px;
        background: #AF0011;
        color: red !important
      }

      /* Add media queries for smaller screens 
      @media screen and (max-width:720px) {
        .weekdays li, .days li {width: 13.1%;}
      }

      @media screen and (max-width: 420px) {
        .weekdays li, .days li {width: 12.5%;}
        .days li .active {padding: 2px;}
      }

      @media screen and (max-width: 290px) {
        .weekdays li, .days li {width: 12.2%;}
      }
      

</style>
<div class="month">      
  <ul>
    <li class="prev">&#10094;</li>
    <li class="next">&#10095;</li>
    <li>
      January<br>
      <span style="font-size:18px">2023</span>
    </li>
  </ul>
</div>

<ul class="weekdays">
  <li>Mo</li>
  <li>Tu</li>
  <li>We</li>
  <li>Th</li>
  <li>Fr</li>
  <li>Sa</li>
  <li>Su</li>
</ul>

<ul class="days">  
  <li>1</li>
  <li>2</li>
  <li>3</li>
  <li>4</li>
  <li>5</li>
  <li>6</li>
  <li>7</li>
  <li>8</li>
  <li>9</li>
  <li><span class="active">18</span></li>
  <li>11</li>
  <li>12</li>
  <li>13</li>
  <li>14</li>
  <li>15</li>
  <li>16</li>
  <li>17</li>
  <li>18</li>
  <li>19</li>
  <li>20</li>
  <li>21</li>
  <li>22</li>
  <li>23</li>
  <li>24</li>
  <li>25</li>
  <li>26</li>
  <li>27</li>
  <li>28</li>
  <li>29</li>
  <li>30</li>
  <li>31</li>
</ul>








<!--
### Where to?

<a href="https://hsinaditam.github.io/Password_Man/PasswordManager.html">
  <input class ="submit" type="submit" value="Password Manager">
<a href="https://hsinaditam.github.io/Password_Man/">
  <input class ="submit" type="submit" value="Calendar">
<a href="https://hsinaditam.github.io/Password_Man/">
  <input class ="submit" type="submit" value="Notepad">
-->