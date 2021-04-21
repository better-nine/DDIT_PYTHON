package kr.aimaker.web;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import kr.aimaker.mybatis.MyBatisConnectionFactory;
import kr.aimaker.mybatis.SampleDAO;
import kr.aimaker.mybatis.SampleVO;

public class ConSample extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setCharacterEncoding("UTF-8");
		
		HttpSession session = request.getSession();
		String emp_id = (String) session.getAttribute("emp_id");
		
		if(emp_id==null) {
			response.sendRedirect("login.html");
			return;
		} 
		
		SampleDAO dao = new SampleDAO(MyBatisConnectionFactory.getSqlSessionFactory());
		ArrayList<SampleVO> list = null;
		
		try {
			list = (ArrayList<SampleVO>) dao.myselect();
		} catch (Exception e) {
			System.out.println(e);
		}
		System.out.println("리스트 길이 : "+list.size()); 
		
		
		request.setAttribute("list", list);
		
		RequestDispatcher rd = request.getRequestDispatcher("/sample.jsp");
		//여기 괄호 안에다가 주소를 넣어줘야 하는데 톰캣이 자동으로 주소연결해서 만들어주기때문에 우리는 뒤에 붙일 스트링값만 입력한거임 
		rd.forward(request, response);
		
		
		
		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
