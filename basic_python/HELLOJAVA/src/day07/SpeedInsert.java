package day07;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Calendar;

public class SpeedInsert {
	
	public static void main(String[] args) throws Exception {
		

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		
		long now1 = Calendar.getInstance().getTimeInMillis();
		
		for(int i = 0;i<10000;i++) {
			String sql = "insert into sample(col01, col02, col03) values ('4','4','4')";
			int cnt = stmt.executeUpdate(sql);
		}
		
		long now2 = Calendar.getInstance().getTimeInMillis();
				
		stmt.close();
		conn.close();
		

		
		long ellapse = now2 - now1;
		
		System.out.println("ellapse: "+ellapse);
		
		
		
		
		

	}
	
	
}
