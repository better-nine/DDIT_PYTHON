package net.ivyro.naeun;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.sun.org.apache.xml.internal.serialize.Printer;

 
public class Temp1Con extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setCharacterEncoding("UTF-8");
		//이건 한글로 변환을 도와주는 코드임. getWriter()보다 위쪽에 있어야 함 꼭! 

		PrintWriter out = response.getWriter();
							// response는 서버가 클라이언트에게 응답한다는 의미를 가진 객체
							//서버가 클라이언트에 response하려면 무조건 response객체를 통해 작업해야함
							//getWriter()는 출력을 통해서 응답하겠다는 메서드임
		//이제 뭔가 출력을 하고 싶을 땐
		out.print("<html>");
		out.print("<head>");					//html태그로 감싸서
		out.print("<meta charset='UTF-8'>"); //이게 있어야 한글로 변환되어서 출력이 됨
		out.print("</head>");
		out.print("<body>");
		out.print("이렇게 출력을 하면 됨");
		out.print("<br/>엔터를 치고 싶으면 html 방식으로 넣어줘야함");
		out.print("</body>");
		out.print("</html>");
		//그런데 여기서 이렇게 출력하는 것 보다 jsp랑 연결해서 출력하는게 훨씬 더 편함
		//jps랑 연결할때는 위에 있는 PrinterWriter객체가 필요하지 않음! ! ! 와! !! 
				
		
		//jsp랑 연결할때는 jsp쪽으로 데이터를 보내주기면 하면 됨.
		//그러면 데이터들이 들어있는 클래스를 포함하고 데이터 호출하는 메서드를 실행함
		Temp1DAO dao = new Temp1DAO();
		
		//실행할 메서드의 리턴값이 리스트이기 때문에 리스트를 먼저 만들어주고
		ArrayList<Temp1VO> list = null;
		
		try {
			list = dao.myselect(); //잘 넣어줌
		} catch (Exception e) {
			//e.printStackTrace();
			System.out.println(e);
		} 
		
		//그래서 저기 데이터 객체가 왕창 들어있는 리스트를 jsp쪽으로 보내주면 됨
		//아래와 같은 식으로 보내줄 수 있음
		request.setAttribute("list", list);
		RequestDispatcher rd = request.getRequestDispatcher("/temp1con.jsp");
	    rd.forward(request, response);
		//이제 이 다음은 jsp에서 마저 진행하면 됨
		
		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
