package ncs.partner.util;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.naver.web.EmpDAO;
import com.naver.web.EmpVO;
 
public class AjaxInsert extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String emp_id 	= request.getParameter("emp_id");
		String emp_name = request.getParameter("emp_name");
		String sex 		= request.getParameter("sex");
		String mobile	= request.getParameter("mobile");
		String address  = request.getParameter("address");

		System.out.println(emp_id);
		System.out.println(emp_name);
		System.out.println(sex);
		System.out.println(mobile);
		System.out.println(address);
		
		EmpVO vo = new EmpVO();
		vo.setEmp_id(emp_id);
		vo.setEmp_name(emp_name);
		vo.setSex(sex);
		vo.setMobile(mobile);
		vo.setAddress(address);
		
		EmpDAO dao = new EmpDAO();
		int cnt = 0;
		
		try {
			cnt = dao.myinsert(vo);
			if(cnt==1) {
				AjaxUtil.responseJson(response, "ok");				
			} else {
				AjaxUtil.responseJson(response, "ng");				
			}
		} catch (Exception e1) {
			System.out.println(e1);
		}
				
		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	
		doGet(request, response);
	}

}
