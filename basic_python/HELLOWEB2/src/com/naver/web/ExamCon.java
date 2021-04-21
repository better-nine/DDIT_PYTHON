package com.naver.web;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class ExamCon extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {


		response.setCharacterEncoding("UTF-8");
	
		EmpExamDAO dao = new EmpExamDAO();
		ArrayList<EmpExamVO> list = null;
		
		try {
			list = dao.myselect();
		} catch (Exception e) {
			System.out.println(e);
		}

		request.setAttribute("list", list);
		
		RequestDispatcher rd = request.getRequestDispatcher("/examcon.jsp");
														//여기 괄호 안에다가 주소를 넣어줘야 하는데 톰캣이 자동으로 주소연결해서 만들어주기때문에 우리는 뒤에 붙일 스트링값만 입력한거임 
	    rd.forward(request, response);
		
		
		
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
