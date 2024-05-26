<%@ page import="java.sql.*" %>
<%
int uname=Integer.parseInt(request.getParameter("uname"));
int pwd =Integer.parseInt(request.getParameter("pwd"));

try {
	
	Class.forName("com.mysql.jdbc.Driver");
	
Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","srujan");

PreparedStatement pstmt = con.prepareStatement(" select role from emp_profile where username=?");
pstmt.setInt(1,uname);

ResultSet rs = pstmt.executeQuery();


while(rs.next())
{
 String role=rs.getString(1);
 session.setAttribute("uname", uname);
 session.setMaxInactiveInterval(20);
 if(role.equals("user"))
 {
	 response.sendRedirect("EmpHome.html");
 }
 else
 {
	 response.sendRedirect("AdminHome.html");
 }

}
  con.close();

}
catch(Exception e)
{
	
}
%>