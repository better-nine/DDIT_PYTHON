package day07;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class MyPreDelete {
	public static void main(String[] args) throws Exception {
		

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		String sql = "delete from sample where col01='1'";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		System.out.println("cnt:"+cnt);
		
		stmt.close();
		conn.close();
		

	}
}
