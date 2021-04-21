package kr.aimaker.web;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.aimaker.mybatis.MyBatisConnectionFactory;
import kr.aimaker.mybatis.SampleDAO;
import kr.aimaker.mybatis.SampleVO;
import kr.aimaker.web.AjaxUtil;
 
public class SampleAjaxInsert extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		String col01 	= request.getParameter("col01");
		String col02 	= request.getParameter("col02");
		String col03 	= request.getParameter("col03");

		System.out.println(col01);
		System.out.println(col02);
		System.out.println(col03); 
		
		SampleVO vo = new SampleVO();
		vo.setCol01(col01);
		vo.setCol02(col02);
		vo.setCol03(col03);
		
		SampleDAO dao = new SampleDAO(MyBatisConnectionFactory.getSqlSessionFactory());
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
