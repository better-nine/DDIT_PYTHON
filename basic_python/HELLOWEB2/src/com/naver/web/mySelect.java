package com.naver.web;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.ResultSet;  
import java.sql.Statement;


public class mySelect {
		
	public static void main(String[] args) throws Exception {
		

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; //oracle expression(평가판)버전은 xe / 회사에서는 orcl이 대부분
		String sql = "select s_code, s_name, cprice, in_time from STOCK where s_name='삼성전자'";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		
		//rs.next() : 뒤에 데이터가 있는지 여부를 물음
		
		
		while (rs.next()) {
			String s_code = rs.getString("s_code");
			String s_name = rs.getString("s_name");
			String cprice = rs.getString("cprice");
			String in_time = rs.getString("in_time");
			
			System.out.print("s_code : "+ s_code);
			System.out.print("s_name : "+ s_name);
			System.out.print(" cprice : "+ cprice);
			System.out.println(" in_time : "+ in_time);
		}
		
		stmt.close();
		conn.close();
		

	}
}
