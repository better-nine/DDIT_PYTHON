<%@page import="com.naver.web.EmpVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<%out.println("hello"); %>
<%="hello" %>
<%=request.getAttribute("a")%>
<% ArrayList<EmpVO> list = (ArrayList<EmpVO>)request.getAttribute("list");%>

<%for(int i = 0 ; i < list.size() ; i++){
	EmpVO tempvo = list.get(i);
%>
<%=tempvo.getEmp_id() %>
<%=tempvo.getEmp_name() %>
	
	
<% }%>


</body>
</html>
