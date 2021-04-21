package ncs.partner.util;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.naver.web.EmpExamDAO;
import com.naver.web.EmpExamVO;
 
public class AjaxExamUpdate extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		String emp_id 	= request.getParameter("emp_id");
		String exam_id = request.getParameter("exam_id");
		String kor 		= request.getParameter("kor");
		String eng	= request.getParameter("eng");
		String mat  = request.getParameter("mat");

		System.out.println(emp_id);
		System.out.println(exam_id);
		System.out.println(kor);
		System.out.println(eng);
		System.out.println(mat);
		
		EmpExamVO vo = new EmpExamVO();
		vo.setEmp_id(emp_id);
		vo.setExam_id(exam_id);
		vo.setKor(kor);
		vo.setEng(eng);
		vo.setMat(mat);
		
		EmpExamDAO dao = new EmpExamDAO();
		int cnt = 0;
		
		try {
			cnt = dao.myupdate(vo);
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
