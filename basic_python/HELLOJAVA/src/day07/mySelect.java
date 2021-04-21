package day07;

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
		String sql = "select col01, col02, col03 from sample";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		
		//rs.next() : 뒤에 데이터가 있는지 여부를 물음
		
		
		while (rs.next()) {
			String col01 = rs.getString("col01");
			String col02 = rs.getString("col02");
			String col03 = rs.getString("col03");
			
			System.out.print("col01 : "+ col01);
			System.out.print(" col02 : "+ col02);
			System.out.println(" col03 : "+ col03);
		}
		
		stmt.close();
		conn.close();
		

	}
}
