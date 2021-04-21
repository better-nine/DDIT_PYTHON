<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%
// 	String dan = request.getParameter("dan");	
	
// 	out.print(dan + "*" + 2 + "=" + Integer.parseInt(dan)*2 + "<br>"); //out<이거 객체래 
// 	out.print(dan + "*" + 3 + "=" + Integer.parseInt(dan)*3 + "<br>");  
// 	out.print(dan + "*" + 4 + "=" + Integer.parseInt(dan)*4 + "<br>");  
// 	out.print(dan + "*" + 5 + "=" + Integer.parseInt(dan)*5 + "<br>");  
// 	out.print(dan + "*" + 6 + "=" + Integer.parseInt(dan)*6 + "<br>");  
// 	out.print(dan + "*" + 7 + "=" + Integer.parseInt(dan)*7 + "<br>");  
// 	out.print(dan + "*" + 8 + "=" + Integer.parseInt(dan)*8 + "<br>");  
// 	out.print(dan + "*" + 9 + "=" + Integer.parseInt(dan)*9 + "<br>");  
	
	
	//jsp에서는 \n \r 둘 다 안먹어서 <br>로 해줘야 엔터쳐짐 
%>

    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>title</title>
</head>
<body>
hello naeun<br>

<% 

	String dan = request.getParameter("dan");
	int i_dan = Integer.parseInt(dan);
	out.print(i_dan + "* 1 = " + i_dan*1+"<br>");
	out.print(i_dan + "* 2 = " + i_dan*2+"<br>");
	out.print(i_dan + "* 3 = " + i_dan*3+"<br>");
	out.print(i_dan + "* 4 = " + i_dan*4+"<br>");
	out.print(i_dan + "* 5 = " + i_dan*5+"<br>");
	out.print(i_dan + "* 6 = " + i_dan*6+"<br>");
	out.print(i_dan + "* 7 = " + i_dan*7+"<br>");
	out.print(i_dan + "* 8 = " + i_dan*8+"<br>");
	out.print(i_dan + "* 9 = " + i_dan*9+"<br>");

%>

</body>
</html>