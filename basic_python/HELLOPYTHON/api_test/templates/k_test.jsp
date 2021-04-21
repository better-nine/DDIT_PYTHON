<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">
<title>Insert title here</title>

<script type="text/javascript">



</script>

</head>
<body>


<% request.setCharacterEncoding("UTF-8"); %>
<% String file = request.getParameter("file"); %>
<% String text = request.getParameter("text"); %>

<%=file %>

</body>
</html>