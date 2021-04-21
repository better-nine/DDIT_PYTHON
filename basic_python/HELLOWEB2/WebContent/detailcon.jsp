<%@page import="com.naver.web.DetailVO"%>
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

	function setData(e_seq, exam_id, question, q1, q2, q3, q4,answer){
		$('#e_seq').val(e_seq);
		$('#exam_id').val(exam_id);
		$('#question').val(question);
		$('#q1').val(q1);
		$('#q2').val(q2);
		$('#q3').val(q3);
		$('#q4').val(q4);
		$('#answer').val(answer);
		
	}


	function fn_add(){
// 		alert("gd")
		var e_seq = $('#e_seq').val();
		var exam_id = $('#exam_id').val();
		var question = $('#question').val();
		var q1 = $('#q1').val();
		var q2 = $('#q2').val();
		var q3 = $('#q3').val();
		var q4 = $('#q4').val();
		var answer = $('#answer').val();
		
		
		
		var param = "";
		param += "dummy=" + Math.random(); //브라우저가 캐시 저장할때 같은 사이트 주소값을 저장하지 않을 수 있게 랜덤값 넣어준거임 
										   //ajax가 똑같은 주소의 브라우저를 받으면 기존에 캐시로 저장했던 페이지 먼저 출력함 (인터넷익스플로러 옵션에서 확인해 볼 수 있는 설정) 
		param += "&e_seq="+e_seq;
		param += "&exam_id="+exam_id;
		param += "&question="+question;
		param += "&q1="+q1;
		param += "&q2="+q2;
		param += "&q3="+q3;
		param += "&q4="+q4;
		param += "&answer="+answer;
		
// 		console.log(e_seq)
		
		$.ajax({
			url : "detailinsert.ajax", //ajax로 불러올 때 ajaxutil 파일이 꼭 필요함. 그 친구가 위쪽 파일 타입을 바꿔줌 
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
// 		alert("gd")
		var e_seq = $('#e_seq').val();
		var exam_id = $('#exam_id').val();
		var question = $('#question').val();
		var q1 = $('#q1').val();
		var q2 = $('#q2').val();
		var q3 = $('#q3').val();
		var q4 = $('#q4').val();
		var answer = $('#answer').val();
		
		
		
		var param = "";
		param += "dummy=" + Math.random(); //브라우저가 캐시 저장할때 같은 사이트 주소값을 저장하지 않을 수 있게 랜덤값 넣어준거임 
										   //ajax가 똑같은 주소의 브라우저를 받으면 기존에 캐시로 저장했던 페이지 먼저 출력함 (인터넷익스플로러 옵션에서 확인해 볼 수 있는 설정) 
		param += "&e_seq="+e_seq;
		param += "&exam_id="+exam_id;
		param += "&question="+question;
		param += "&q1="+q1;
		param += "&q2="+q2;
		param += "&q3="+q3;
		param += "&q4="+q4;
		param += "&answer="+answer;
		
// 		console.log(e_seq)
		
		$.ajax({
			url : "detailupdate.ajax", //ajax로 불러올 때 ajaxutil 파일이 꼭 필요함. 그 친구가 위쪽 파일 타입을 바꿔줌 
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
// 		alert("gd")
		var e_seq = $('#e_seq').val();
		var exam_id = $('#exam_id').val();
		
		var param = "";
		param += "dummy=" + Math.random(); //브라우저가 캐시 저장할때 같은 사이트 주소값을 저장하지 않을 수 있게 랜덤값 넣어준거임 
										   //ajax가 똑같은 주소의 브라우저를 받으면 기존에 캐시로 저장했던 페이지 먼저 출력함 (인터넷익스플로러 옵션에서 확인해 볼 수 있는 설정) 
		param += "&e_seq="+e_seq;
		param += "&exam_id="+exam_id;
		
// 		console.log(e_seq)
		
		$.ajax({
			url : "detaildelete.ajax", //ajax로 불러올 때 ajaxutil 파일이 꼭 필요함. 그 친구가 위쪽 파일 타입을 바꿔줌 
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




<% ArrayList<DetailVO> list = (ArrayList<DetailVO>)request.getAttribute("list");%>

<table border='2'>
 <tr>
   <td>
	<table border='1'>
		<tr>
			<th>순번</th>
			<th>수험번호</th>
			<th>질문</th>
			<th>1번</th>
			<th>2번</th>
			<th>3번</th>
			<th>4번</th>
			<th>답변</th>
		</tr>
	<%for(int i = 0 ; i < list.size() ; i++){
		DetailVO tempvo = list.get(i);
	%>
		<tr>
			<td><a href="javascript:setData('<%=tempvo.getE_seq() %>','<%=tempvo.getExam_id() %>','<%=tempvo.getQuestion()%>','<%=tempvo.getQ1()%>','<%=tempvo.getQ2()%>','<%=tempvo.getQ3()%>','<%=tempvo.getQ4()%>','<%=tempvo.getAnswer()%>')"><%=tempvo.getE_seq() %>,<%=tempvo.getExam_id() %></a></td>
			<td><%=tempvo.getExam_id()%></td>
			<td><%=tempvo.getQuestion()%></td>
			<td><%=tempvo.getQ1()%></td>
			<td><%=tempvo.getQ2()%></td>
			<td><%=tempvo.getQ3()%></td>
			<td><%=tempvo.getQ4()%></td>
			<td><%=tempvo.getAnswer()%></td>	
		</tr>
	
	<% }%>
	</table>	
   </td>

   <td>
   	<table>
   		<tr>
   			<th>순번</th>
   			<th>
   				<input type='text' id='e_seq'>
   			</th> 		
   		</tr>
   		<tr>
   			<th>수험번호</th>
   			<th>
   				<input type='text' id='exam_id'>
   			</th>  		
   		</tr>
   		<tr>
   			<th>질문</th>
   			<th>
   				<input type='text' id='question'>
   			</th>  		
   		</tr>
   		<tr>
   			<th>1번</th>
   			<th>
   				<input type='text' id='q1'>
   			</th>  		
   		</tr>
   		<tr>
   			<th>2번</th>
   			<th>
   				<input type='text' id='q2'>
   			</th>  		
   		</tr>
		<tr>
   			<th>3번</th>
   			<th>
   				<input type='text' id='q3'>
   			</th>  		
   		</tr>
   		<tr>
   			<th>4번</th>
   			<th>
   				<input type='text' id='q4'>
   			</th>  		
   		</tr>
			<tr>
   			<th>답변</th>
   			<th>
   				<input type='text' id='answer'>
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