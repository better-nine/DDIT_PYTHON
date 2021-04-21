<%@page import="com.naver.web.EmpExamVO"%>
<%@page import="com.naver.web.EmpExamDAO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<style type="text/css">

table {
	border-collapse : collapse;
}

</style>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="jquery-3.5.1.js"></script>
<script type="text/javascript">

	function setData(emp_id, exam_id, kor, eng, mat){
		$('#emp_id').val(emp_id);
		$('#exam_id').val(exam_id);
		$('#kor').val(kor);
		$('#eng').val(eng);
		$('#mat').val(mat);
	
	}

	function fn_add(){
		var emp_id = $('#emp_id').val();
		var exam_id = $('#exam_id').val();
		var kor = $('#kor').val();
		var eng = $('#eng').val();
		var mat = $('#mat').val();
		
		var param = "";
		param += "dummy=" + Math.random(); //브라우저가 캐시 저장할때 같은 사이트 주소값을 저장하지 않을 수 있게 랜덤값 넣어준거임 
										   //ajax가 똑같은 주소의 브라우저를 받으면 기존에 캐시로 저장했던 페이지 먼저 출력함 (인터넷익스플로러 옵션에서 확인해 볼 수 있는 설정) 
		param += "&emp_id="+emp_id;
		param += "&exam_id="+exam_id;
		param += "&kor="+kor;
		param += "&eng="+eng;
		param += "&mat="+mat;
		
		
		$.ajax({
			url : "examinsert.ajax", //ajax로 불러올 때 ajaxutil 파일이 꼭 필요함. 그 친구가 위쪽 파일 타입을 바꿔줌 
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
		var emp_id = $('#emp_id').val();
		var exam_id = $('#exam_id').val();
		var kor = $('#kor').val();
		var eng = $('#eng').val();
		var mat = $('#mat').val();
		
		var param = "";
		param += "dummy=" + Math.random(); //브라우저가 캐시 저장할때 같은 사이트 주소값을 저장하지 않을 수 있게 랜덤값 넣어준거임 
										   //ajax가 똑같은 주소의 브라우저를 받으면 기존에 캐시로 저장했던 페이지 먼저 출력함 (인터넷익스플로러 옵션에서 확인해 볼 수 있는 설정) 
		param += "&emp_id="+emp_id;
		param += "&exam_id="+exam_id;
		param += "&kor="+kor;
		param += "&eng="+eng;
		param += "&mat="+mat;
		
		
		$.ajax({
			url : "examupdate.ajax", //ajax로 불러올 때 ajaxutil 파일이 꼭 필요함. 그 친구가 위쪽 파일 타입을 바꿔줌 
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
		var emp_id = $('#emp_id').val();
		var exam_id = $('#exam_id').val();
		
		var param = "";
		param += "dummy=" + Math.random(); //브라우저가 캐시 저장할때 같은 사이트 주소값을 저장하지 않을 수 있게 랜덤값 넣어준거임 
										   //ajax가 똑같은 주소의 브라우저를 받으면 기존에 캐시로 저장했던 페이지 먼저 출력함 (인터넷익스플로러 옵션에서 확인해 볼 수 있는 설정) 
		param += "&emp_id="+emp_id;
		param += "&exam_id="+exam_id;
		
		
		$.ajax({
			url : "examdelete.ajax", //ajax로 불러올 때 ajaxutil 파일이 꼭 필요함. 그 친구가 위쪽 파일 타입을 바꿔줌 
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


<% ArrayList<EmpExamVO> list = (ArrayList<EmpExamVO>)request.getAttribute("list");%>

<table border='2'>
 <tr>
   <td>
	<table border='1'>
		<tr>
			<th>사원번호</th>
			<th>수험번호</th>
			<th>국어</th>
			<th>영어</th>
			<th>수학</th>
		</tr>
	<%for(int i = 0 ; i < list.size() ; i++){
		EmpExamVO tempvo = list.get(i);
	%>
		<tr>
			<td><a href="javascript:setData('<%=tempvo.getEmp_id() %>','<%=tempvo.getExam_id() %>','<%=tempvo.getKor()%>','<%=tempvo.getEng()%>','<%=tempvo.getMat()%>')"><%=tempvo.getEmp_id() %>,<%=tempvo.getExam_id()%></a></td>
			<td><%=tempvo.getExam_id()%></td>
			<td><%=tempvo.getKor()%></td>
			<td><%=tempvo.getEng()%></td>	
			<td><%=tempvo.getMat()%></td>	
		</tr>
	
	<% }%>
	</table>	
   </td>

   <td>
   	<table>
   		<tr>
   			<th>사원번호</th>
   			<th>
   				<input type='text' id='emp_id'>
   			</th> 		
   		</tr>
   		<tr>
   			<th>수험번호</th>
   			<th>
   				<input type='text' id='exam_id'>
   			</th>  		
   		</tr>
   		<tr>
   			<th>국어</th>
   			<th>
   				<input type='text' id='kor'>
   			</th>  		
   		</tr>
   		<tr>
   			<th>영어</th>
   			<th>
   				<input type='text' id='eng'>
   			</th>  		
   		</tr>
   		<tr>
   			<th>수학</th>
   			<th>
   				<input type='text' id='mat'>
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