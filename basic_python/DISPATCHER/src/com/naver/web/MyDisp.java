package com.naver.web;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class MyDisp extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//		PrintWriter out = response.getWriter(); 글씨출력할때 쓰는거라 필요없어짐
		
		ArrayList<EmpVO> list = new ArrayList<EmpVO>();
		
		{
			EmpVO tempvo = new EmpVO();
			tempvo.setEmp_id("1");
			tempvo.setEmp_name("홍길동");
			list.add(tempvo);
		}
		{
			EmpVO tempvo = new EmpVO();
			tempvo.setEmp_id("2");
			tempvo.setEmp_name("김현주");
			list.add(tempvo);
		}
		
		request.setAttribute("list", list);
		request.setAttribute("a", "hello");
		
		RequestDispatcher rd = request.getRequestDispatcher("/mydisp.jsp");
	    rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
