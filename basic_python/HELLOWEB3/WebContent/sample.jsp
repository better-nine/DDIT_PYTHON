<%@page import="kr.aimaker.mybatis.SampleVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">

table {
	border-collapse : collapse;
}


</style>

<script src="jquery-3.5.1.js"></script>
<script type="text/javascript">

	function setData(col01, col02, col03){
		$('#col01').val(col01);
		$('#col02').val(col02);
		$('#col03').val(col03);
		console.log(col01)
	}
	
	function fn_add(){
		var col01 = $('#col01').val();
		var col02 = $('#col02').val();
		var col03 = $('#col03').val();
		
		var param = "";
		param += "dummy=" + Math.random(); //브라우저가 캐시 저장할때 같은 사이트 주소값을 저장하지 않을 수 있게 랜덤값 넣어준거임 
										   //ajax가 똑같은 주소의 브라우저를 받으면 기존에 캐시로 저장했던 페이지 먼저 출력함 (인터넷익스플로러 옵션에서 확인해 볼 수 있는 설정) 
		param += "&col01="+col01;
		param += "&col02="+col02;
		param += "&col03="+col03;
		
		
		$.ajax({
			url : "sampleinsert.ajax", //ajax로 불러올 때 ajaxutil 파일이 꼭 필요함. 그 친구가 위쪽 파일 타입을 바꿔줌 
			data : param,
			dataType : "json",
			type : "post",
			async: false,
			statusCode : {
				404 : function() {
					alert("네트워크가 불안정합니다. 다시 시도부탁드립니다.");
				}
			},
			success : function(data) {
				fn_add_callback(data);
			}
		});
	}	
	function fn_add_callback(data){ //얘가 메시지 띄우게 도와주는 코드 
		if(data == null){
			return;
		}
		alert(data);
		if(data=="ok"){
			alert("정상적으로 추가되었습니다.");
			location.reload(); //화면 자동으로 새로고침 해주는 기능!!!! 
		} else {
			alert("추가 도중 문제가 생겼습니다.");			
		}
				
	}
	
	function fn_upd(){
		var col01 = $('#col01').val();
		var col02 = $('#col02').val();
		var col03 = $('#col03').val();
		
		var param = "";
		param += "dummy=" + Math.random(); //브라우저가 캐시 저장할때 같은 사이트 주소값을 저장하지 않을 수 있게 랜덤값 넣어준거임 
										   //ajax가 똑같은 주소의 브라우저를 받으면 기존에 캐시로 저장했던 페이지 먼저 출력함 (인터넷익스플로러 옵션에서 확인해 볼 수 있는 설정) 
		param += "&col01="+col01;
		param += "&col02="+col02;
		param += "&col03="+col03;
		
		
		$.ajax({
			url : "sampleupdate.ajax", //ajax로 불러올 때 ajaxutil 파일이 꼭 필요함. 그 친구가 위쪽 파일 타입을 바꿔줌 
			data : param,
			dataType : "json",
			type : "post",
			async: false,
			statusCode : {
				404 : function() {
					alert("네트워크가 불안정합니다. 다시 시도부탁드립니다.");
				}
			},
			success : function(data) {
				fn_upd_callback(data);
			}
		});
	}	
	function fn_upd_callback(data){ //얘가 메시지 띄우게 도와주는 코드 
		if(data == null){
			return;
		}
		alert(data);
		if(data=="ok"){
			alert("정상적으로 수정되었습니다.");
			location.reload(); //화면 자동으로 새로고침 해주는 기능!!!! 
		} else {
			alert("수정 도중 문제가 생겼습니다.");			
		}
				
	}
	
	function fn_del(){
		var col01 = $('#col01').val();

		var param = "";
		param += "dummy=" + Math.random(); //브라우저가 캐시 저장할때 같은 사이트 주소값을 저장하지 않을 수 있게 랜덤값 넣어준거임 
										   //ajax가 똑같은 주소의 브라우저를 받으면 기존에 캐시로 저장했던 페이지 먼저 출력함 (인터넷익스플로러 옵션에서 확인해 볼 수 있는 설정) 
		param += "&col01="+col01;
		 
		
		
		$.ajax({
			url : "sampledelete.ajax", //ajax로 불러올 때 ajaxutil 파일이 꼭 필요함. 그 친구가 위쪽 파일 타입을 바꿔줌 
			data : param,
			dataType : "json",
			type : "post",
			async: false,
			statusCode : {
				404 : function() {
					alert("네트워크가 불안정합니다. 다시 시도부탁드립니다.");
				}
			},
			success : function(data) {
				fn_del_callback(data);
			}
		});
	}	
	function fn_del_callback(data){ //얘가 메시지 띄우게 도와주는 코드 
		if(data == null){
			return;
		}
		alert(data);
		if(data=="ok"){
			alert("정상적으로 삭제되었습니다.");
			location.reload(); //화면 자동으로 새로고침 해주는 기능!!!! 
		} else {
			alert("삭제 도중 문제가 생겼습니다.");			
		}
				
	}


</script>


</head>
<body>


<% ArrayList<SampleVO> list = (ArrayList<SampleVO>)request.getAttribute("list");%>

<table border='2'>
 <tr>
   <td>
	<table border='1'>
		<tr>
			<th>col01</th>
			<th>col02</th>
			<th>col03</th>
		</tr>
	<%for(int i = 0 ; i < list.size() ; i++){
		SampleVO tempvo = list.get(i);
	%>
		<tr>
			<td><a href="javascript:setData('<%=tempvo.getCol01()%>','<%=tempvo.getCol02()%>','<%=tempvo.getCol03()%>')"><%=tempvo.getCol01()%></a></td>
			<td><%=tempvo.getCol02()%></td>
			<td><%=tempvo.getCol03()%></td>
		</tr>
	<% }%>
	</table>	
   </td>

   <td>
   	<table>
   		<tr>
   			<th>col01</th>
   			<th>
   				<input type='text' id='col01'>
   			</th> 		
   		</tr>
   		<tr>
   			<th>col02</th>
   			<th>
   				<input type='text' id='col02'>
   			</th>  		
   		</tr>
   		<tr>
   			<th>col03</th>
   			<th>
   				<input type='text' id='col03'>
   			</th>  		
   		</tr>
   		<tr>
   			<th colspan='2'>
   				<input type='button' value='등록' onclick='fn_add()'>
   				<input type='button' value='수정' onclick='fn_upd()'>
   				<input type='button' value='삭제' onclick='fn_del()'>
   			</th>
   		</tr>   	
   	</table>
   </td>
	
 </tr>

</table>


</body>
</html>