package ncs.partner.util;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.naver.web.EmpDAO;
import com.naver.web.EmpVO;

public class AjaxDelete extends HttpServlet {
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		String emp_id 	= request.getParameter("emp_id");

		System.out.println(emp_id);
		
		EmpVO vo = new EmpVO();
		vo.setEmp_id(emp_id);
		
		EmpDAO dao = new EmpDAO();
		int cnt = 0;
		
		try {
			cnt = dao.mydelete(vo);
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
