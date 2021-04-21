<%@page import="net.ivyro.naeun.Temp1DAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>


<%
	request.setCharacterEncoding("UTF-8");


//ajax에서 요청한 데이터 받아오기
String id = request.getParameter("id");
String pass = request.getParameter("pass");
String name = request.getParameter("name");



String jdata = "insert into temp1(user_id, user_pass, user_name) values('"+id+"','"+pass+"','"+name+"')";

Temp1DAO dao = new Temp1DAO();

int cnt = dao.myinsert(jdata);


%>
    
    
    