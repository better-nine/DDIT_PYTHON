package ncs.partner.util;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.naver.web.DetailDAO;
import com.naver.web.DetailVO;
public class AjaxDetailDelete extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	


		String e_seq 	= request.getParameter("e_seq");
		String exam_id = request.getParameter("exam_id");

		System.out.println(e_seq);
		System.out.println(exam_id);
		
		DetailVO vo = new DetailVO();
		vo.setE_seq(e_seq);
		vo.setExam_id(exam_id);
		
		
		DetailDAO dao = new DetailDAO();
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
