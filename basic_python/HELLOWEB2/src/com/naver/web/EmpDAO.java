package com.naver.web;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class EmpDAO {
	
	public ArrayList<EmpVO> myselect() throws Exception{
		
		ArrayList<EmpVO> list = new ArrayList<EmpVO>();
		
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; //oracle expression(평가판)버전은 xe / 회사에서는 orcl이 대부분
		String sql = "select emp_id, emp_name, sex, mobile, address from emp";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		
		
		while (rs.next()) {
			String emp_id = rs.getString(1); //column명 말고 index순번을 적어도 됨
			String emp_name = rs.getString("emp_name");
			String sex = rs.getString("sex");
			String mobile = rs.getString("mobile");
			String address = rs.getString("address");
			
			EmpVO tempvo = new EmpVO();
			tempvo.setEmp_id(emp_id);
			tempvo.setEmp_name(emp_name);
			tempvo.setSex(sex);
			tempvo.setMobile(mobile);
			tempvo.setAddress(address);
		
			list.add(tempvo);		
		}
		
		stmt.close();
		conn.close();

		return list;
	}
	
	public int myinsert(EmpVO vo) throws Exception{
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		
		String sql = "insert into emp (emp_id, emp_name, sex, mobile, address) "
				+ "values ('"+vo.getEmp_id()+"','"+vo.getEmp_name()+"','"+vo.getSex()+"','"+vo.getMobile()+"','"+vo.getAddress()+"')";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		
		return cnt; //성공시 1 반환
	}

	public int myupdate(EmpVO vo) throws Exception{
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		
		String sql = "update emp "
				+ "set emp_name='"+vo.getEmp_name()+"', sex='"+vo.getSex()+"', mobile='"+vo.getMobile()+"',"
						+ " address='"+vo.getAddress()+"' where emp_id='"+vo.getEmp_id()+"'";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		
		return cnt; //성공시 1 반환
	}
	
	public int mydelete(EmpVO vo) throws Exception{
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		
		String sql = "delete emp where emp_id='"+vo.getEmp_id()+"'";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		
		return cnt; //성공시 1 반환
	}
	
	
	
	public static void main(String[] args) throws Exception  {
		
		EmpDAO dao = new EmpDAO();
		ArrayList<EmpVO> emplist = dao.myselect();
		
		for(int i = 0 ; i < emplist.size() ; i++) {
			EmpVO tempvo = emplist.get(i);
		
			System.out.println(tempvo.getEmp_id());
			System.out.println(tempvo.getEmp_name());
			System.out.println(tempvo.getSex());
			System.out.println(tempvo.getMobile());
			System.out.println(tempvo.getAddress());
		
		}
//-------------------------------------------------------------		
//		EmpVO vo = new EmpVO();
//		
//		vo.setEmp_id("admin");
//		vo.setEmp_name("naeun");
//		vo.setSex("F");
//		vo.setMobile("010-8665-7286");
//		vo.setAddress("세종시");
//		
//		int cnt = dao.myinsert(vo);
//		System.out.println(cnt);
		
		
	}
	
	
	
	
	
	
}
