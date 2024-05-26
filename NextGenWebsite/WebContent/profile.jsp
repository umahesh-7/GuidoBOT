<%@page import="java.sql.*"%>
<%

int uname=(int)session.getAttribute("uname");
//int uid=Integer.parseInt(uname);
try {
	
	Class.forName("com.mysql.jdbc.Driver");
	
Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","srujan");

PreparedStatement pstmt = con.prepareStatement(" select * from emp_profile where username=?");
pstmt.setInt(1,uname);

ResultSet rs = pstmt.executeQuery();

while(rs.next())
{
	
%>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 30px 40px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #4CAF50;
}
input[type=text], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
}

label {
  padding: 12px 12px 12px 0;
  display: inline-block;
}

input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: right;
}

input[type=submit]:hover {
  background-color: #45a049;
}

.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}

.col-25 {
  float: left;
  width: 25%;
  margin-top: 6px;
}

.col-75 {
  float: left;
  width: 75%;
  margin-top: 6px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Responsive layout - when the screen is less than 600px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .col-25, .col-75, input[type=submit] {
    width: 100%;
    margin-top: 0;
  }
}
</style>
</head>
<body>

<center> <h1>A NextGen Website</h1></center>
<ul>
  <li><a  href="EmpHome.html">Home</a></li>
  <li><a class="active" href="#">Profile </a></li>
  <li style="float:right"><a  href="logout.jsp">Logout</a></li>
  
</ul>

<div class="container">
  <form action="#">
    <div class="row">
      <div class="col-25">
        <label for="fname">Employee Id</label>
      </div>
      <div class="col-75">
        <input type="text" id="empid" disabled name="id" placeholder=" <%=rs.getInt(1)%>">
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="country">Username</label>
      </div>
      <div class="col-75">
         <input type="text" id="un" disabled name="user" placeholder="<%=rs.getInt(10)%>">
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="lname">Name</label>
      </div>
      <div class="col-75">
        <input type="text" id="fname" disabled name="uname" placeholder="<%=rs.getString(2)%>">
      </div>
    </div>
    
    <div class="row">
      <div class="col-25">
        <label for="subject">Email</label>
      </div>
       <div class="col-75">
        <input type="text" id="emailid" disabled name="email" placeholder="<%=rs.getString(4)%>">
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="subject">Designation</label>
      </div>
       <div class="col-75">
        <input type="text" id="des" disabled name="desg" placeholder="<%=rs.getString(5)%>">
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="subject">Qualification</label>
      </div>
       <div class="col-75">
        <input type="text" id="qualy" disabled name="qual" placeholder="<%=rs.getString(6)%>">
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="subject">Research Publications</label>
      </div>
       <div class="col-75">
        <input type="text" id="reas" disabled name="pub" placeholder="<%=rs.getInt(7)%>">
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="subject">Experience</label>
      </div>
       <div class="col-75">
        <input type="text" id="em" disabled name="exp" placeholder="<%=rs.getInt(8)%>">
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="country">Department</label>
      </div>
      <div class="col-75">
         <input type="text" id="de" disabled name="dept" placeholder="<%=rs.getString(9)%>">
      </div>
    </div>
    
    <div class="row">
      <input type="Submit" value="Update Profile"> &nbsp;&nbsp;&nbsp;
      <input type="Submit" value="Change Password"> 
    </div>
  </form>
</div>

</body>
</html>
	
	
<% 
}
}
catch(Exception e)
{
	
}



%>
