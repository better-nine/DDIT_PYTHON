package com.naver.web;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class EmpExamDAO {
	
	
	public ArrayList<EmpExamVO> myselect() throws Exception{
		
		ArrayList<EmpExamVO> list = new ArrayList<EmpExamVO>();
		
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; //oracle expression(평가판)버전은 xe / 회사에서는 orcl이 대부분
		String sql = "select emp_id, exam_id, kor, eng, mat from empexam";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		
		
		while (rs.next()) {
			String emp_id = rs.getString("emp_id");
			String exam_id = rs.getString("exam_id");
			String kor = rs.getString("kor");
			String eng = rs.getString("eng");
			String mat = rs.getString("mat");
						
			EmpExamVO tempvo = new EmpExamVO();
			tempvo.setEmp_id(emp_id);
			tempvo.setExam_id(exam_id);
			tempvo.setKor(kor);
			tempvo.setEng(eng);
			tempvo.setMat(mat);
		
			list.add(tempvo);		
		}
		
		stmt.close();
		
		conn.close();

		return list;
	}

	public int myinsert(EmpExamVO vo) throws Exception{
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		
		String sql = "insert into empexam(emp_id, exam_id, kor, eng, mat) "
				+ "values ('"+vo.getEmp_id()+"','"+vo.getExam_id()+"','"+vo.getKor()+"','"+vo.getEng()+"','"+vo.getMat()+"')";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		
		return cnt; //성공시 1 반환
	}

	public int myupdate(EmpExamVO vo) throws Exception{
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		
		String sql = "update empexam "
				+ "set kor='"+vo.getKor()+"', eng='"+vo.getEng()+"', mat='"+vo.getMat()+"' "
						+ "where emp_id='"+vo.getEmp_id()+"' and exam_id='"+vo.getExam_id()+"'";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		
		stmt.close();
		conn.close();
		
		return cnt; //성공시 1 반환
	}
	
	public int mydelete(EmpExamVO vo) throws Exception{
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		
		String sql = "delete empexam "
						+ "where emp_id='"+vo.getEmp_id()+"' and exam_id='"+vo.getExam_id()+"'";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		
		stmt.close();
		conn.close();
		
		return cnt; //성공시 1 반환
	}


	public static void main(String[] args) throws Exception {
		
		EmpExamDAO dao = new EmpExamDAO();
		
		EmpExamVO vo = new EmpExamVO();
//		
//		vo.setEmp_id("admin");
//		vo.setExam_id("3");
//		vo.setKor("80");
//		vo.setEng("80");
//		vo.setMat("90");
//		
//		int cnt = dao.myinsert(vo);
//		System.out.println(cnt);
		
//		ArrayList<EmpExamVO> empexamlist = dao.myselect();
//		
//		for(int i = 0 ; i < empexamlist.size() ; i++) {
//			EmpExamVO tempvo = empexamlist.get(i);
//		
//			System.out.println(tempvo.getEmp_id());
//			System.out.println(tempvo.getExam_id());
//		
//		}
		
		
	}

	
}
