package kr.aimaker.web;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import kr.aimaker.mybatis.MyBatisConnectionFactory;
import kr.aimaker.mybatis.SampleDAO;
import kr.aimaker.mybatis.SampleVO;
import kr.aimaker.web.AjaxUtil;
 
public class ConLogin extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		String emp_id 	= request.getParameter("emp_id");
		String pwd	 	= request.getParameter("pwd");
    
		try {
			if(emp_id.equals("1") && pwd.equals("1")) {
				HttpSession session = request.getSession();
				session.setAttribute("emp_id", emp_id);
				session.setAttribute("pwd", pwd);
				
				AjaxUtil.responseJson(response, "ok");				
			} else {
				
				
				AjaxUtil.responseJson(response, "ng");				
			}			
		} catch (Exception e) {
		}
		 
				
	
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
