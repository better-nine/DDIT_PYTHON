<%@page import="net.ivyro.naeun.Temp1VO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>gg</title>
<style>
 table {
 	border-collapse : collapse;
 }
</style>
<script src="jquery-3.5.1.js"></script> 
<script type="text/javascript">
 function getInfo(id, pass, name){
	 $('#id').val(id);
	 $('#pass').val(pass);
	 $('#name').val(name); 
 }
 
 function fn_add(){
	
	 //입력한 값을 가져옴
	 var user_id = $('#id').val().trim();
	 var user_pass = $('#pass').val().trim();
	 var user_name = $('#name').val().trim();
	 
	 //이걸 String타입 변수에 넣어줌
	 vdata = "id="+user_id+"&pass="+user_pass+"&name="+user_name;
	 
	 
	 
	 
	 //console.log(vdata) 입력된 값을 잘 가져오는지 확인해봄 
	 //vdata = $(요소덩어리).serialize(); 이걸 사용하면
	 //위에서 입력한거 전부 필요없이 한번에 가져올 수 있음
	 //만약 json 형식으로 만든다 치면
	 jdata = {
			 "id" : user_id,
			 "pass" : user_pass,
			 "name" : user_name			 
	 }
	 //이렇게 만들면 됨. 이건 json형태임 
	 console.log(jdata)
	 
	 $.ajax({
		
		 url:'temp1-crud.jsp',
		 type : 'post',
		 data : jdata,
		 dataType:'json',
		 success : function(){
			 //테이블 추가되는거 만들어야함
		 },
		 error : function(err){
			 alert("상태:"+err.status);
		 }
	 })
	 
	 
	 
 }
 
 
 
 
</script>
</head>
<body>
<% ArrayList<Temp1VO> list =  (ArrayList<Temp1VO>)request.getAttribute("list");%>
  <table border='1'>
    <tr>
      <td>
	      <table id='user_list' border='1'>
		<tr>
			<th>아이디</th>	
			<th>비밀번호</th>	
			<th>이름</th>	
		</tr>
	
	<% for(int i = 0 ; i < list.size() ; i++){
		Temp1VO tempvo = list.get(i);
	%>	
		<tr>
			<td><a href="javascript:getInfo('<%=tempvo.getUser_id() %>','<%=tempvo.getUser_pass() %>','<%=tempvo.getUser_name() %>')"><%=tempvo.getUser_id() %></a></td>
			<td><%=tempvo.getUser_pass() %></td>
			<td><%=tempvo.getUser_name() %></td>
		</tr>
	<% 	
	}%>
	  	  </table>    
    
      </td>
      <td>
	      <table border='1'>
	    	<tr>
	    	  <th>아이디</th><th><input type="text" id="id" /></th>
	    	</tr>
	    	<tr>
	    	  <th>비밀번호</th><th><input type="text" id="pass" /></th>
	    	</tr>
	    	<tr>
	    	  <th>이름</th><th><input type="text" id="name" /></th>
	    	</tr>
	    	<tr>
	    	  <th colspan='2'><input type="button" value="추가" id="add" onclick="fn_add()"/><input type="button" value="수정" /></th>
	    	</tr>
	      </table>
      </td>
    </tr>
  </table>








</body>
</html>