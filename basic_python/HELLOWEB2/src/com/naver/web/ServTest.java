package com.naver.web;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.ResultSet;  
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class ServTest {
	
	public static void main(String[] args) throws Exception {
		
		
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String sql = "select s_code, s_name, cprice, in_time from STOCK where s_name='삼성전자'"
				+ "order by in_time";
		
		Connection conn = null;
		Statement stmt = null;
		
		try {
			Class.forName(driver);
		} catch (ClassNotFoundException e) {
			
			e.printStackTrace();
		}
		try {
			conn = DriverManager.getConnection(url, "python", "python");
			stmt = conn.createStatement();
			ResultSet rs = stmt.executeQuery(sql);
			while (rs.next()) {
			String col01 = rs.getString(1);
			String col02 = rs.getString(2);
			String col03 = rs.getString(3);
			String col04 = rs.getString(4);
			
			System.out.print("종목번호 : "+ col01);
			System.out.print("종목이름 : "+ col02);
			System.out.print("종목가격 : "+ col03);
			System.out.println("공시시간 : "+ col04);
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				stmt.close();
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}		
	}
	
	
}
