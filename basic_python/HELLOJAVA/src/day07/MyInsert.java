package day07;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class MyInsert {
	
	public static void main(String[] args) throws Exception {
		

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		String sql = "insert into sample(col01, col02, col03) values ('6','6','6')";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		System.out.println("cnt:"+cnt);
		
		stmt.close();
		conn.close();
		

	}
	
	
}
