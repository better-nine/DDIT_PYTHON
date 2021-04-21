package com.naver.web;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class DetailDAO {
	public ArrayList<DetailVO> myselect() throws Exception{
		
		ArrayList<DetailVO> list = new ArrayList<DetailVO>();
		
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; //oracle expression(평가판)버전은 xe / 회사에서는 orcl이 대부분
		String sql = "select e_seq, exam_id, question, answer, q1, q2, q3, q4 from exam_detail";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		
		
		while (rs.next()) {
			String e_seq = rs.getString("e_seq");
			String exam_id = rs.getString("exam_id");
			String question = rs.getString("question");
			String answer = rs.getString("answer");
			String q1 = rs.getString("q1");
			String q2 = rs.getString("q2");
			String q3 = rs.getString("q3");
			String q4 = rs.getString("q4");
			
			DetailVO tempvo = new DetailVO();
			tempvo.setE_seq(e_seq);
			tempvo.setExam_id(exam_id);
			tempvo.setQuestion(question);
			tempvo.setAnswer(answer);
			tempvo.setQ1(q1);
			tempvo.setQ2(q2);
			tempvo.setQ3(q3);
			tempvo.setQ4(q4);
		
			list.add(tempvo);		
		}
		
		stmt.close();
		conn.close();

		return list;
	}
	
	
	public int myinsert(DetailVO vo) throws Exception{
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		
		String sql = "insert into exam_detail (e_seq, exam_id, question, q1, q2, q3, q4, answer) "
				+ "values ('"+vo.getE_seq()+"','"+vo.getExam_id()+"','"+vo.getQuestion()+"','"+vo.getQ1()+"','"+vo.getQ2()+"','"+vo.getQ3()+"','"+vo.getQ4()+"','"+vo.getAnswer()+"')";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		
		return cnt; //성공시 1 반환
	}


	public int myupdate(DetailVO vo) throws Exception{
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		
		String sql = "update exam_detail "
				+ "set question='"+vo.getQuestion()+"', q1='"+vo.getQ1()+"', q2='"+vo.getQ2()+"', q3='"+vo.getQ3()+"', q4='"+vo.getQ4()+"', answer='"+vo.getAnswer()+"'" 
						+ "where e_seq='"+vo.getE_seq()+"' and exam_id='"+vo.getExam_id()+"'";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		
		stmt.close();
		conn.close();
		
		return cnt; //성공시 1 반환
	}
	
	public int mydelete(DetailVO vo) throws Exception{
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		
		String sql = "delete exam_detail "
						+ "where e_seq='"+vo.getE_seq()+"' and exam_id='"+vo.getExam_id()+"'";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		
		stmt.close();
		conn.close();
		
		return cnt; //성공시 1 반환
	}
	
	
	
}
