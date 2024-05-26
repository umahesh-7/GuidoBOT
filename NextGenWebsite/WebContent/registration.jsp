<%@ page import="java.sql.*" %>
<%
int id=Integer.parseInt(request.getParameter("id"));
String uname = request.getParameter("uname");
String gender = request.getParameter("gender");
String email=request.getParameter("email");
String desg=request.getParameter("desg");
String qual=request.getParameter("qual");
int pub =Integer.parseInt(request.getParameter("pub"));
int exp=Integer.parseInt(request.getParameter("exp"));
String dept=request.getParameter("dept");

try {
	
	Class.forName("com.mysql.jdbc.Driver");
	
Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","srujan");

PreparedStatement pstmt = con.prepareStatement("insert into emp_profile values(?,?,?,?,?,?,?,?,?,?,?,?)");
pstmt.setInt(1,id);
pstmt.setString(2,uname);
pstmt.setString(3,gender);
pstmt.setString(4,email);
pstmt.setString(5,desg);
pstmt.setString(6,qual);
pstmt.setInt(7,pub);
pstmt.setInt(8,exp);
pstmt.setString(9,dept);
pstmt.setString(10,Integer.toString(id));
pstmt.setString(11,Integer.toString(id));
pstmt.setString(12,"user");
pstmt.executeUpdate();

 
response.sendRedirect("success.html");
  con.close();

}
catch(Exception e)
{
	
}
%>