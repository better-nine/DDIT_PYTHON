package day07;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Calendar;

public class SpeedPreInsert {
	
	public static void main(String[] args) throws Exception {
		

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; //oracle expression(평가판)버전은 xe / 회사에서는 orcl이 대부분
		String sql = "insert into sample(col01, col02, col03) values(?,?,?)";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		PreparedStatement pstmt = conn.prepareStatement(sql); //얘는 반복문 돌릴 때 속도가 빠름 
		
		
		long now1 = Calendar.getInstance().getTimeInMillis();
		for(int i = 0; i<10000;i++) {
			pstmt.setString(1, "4");
			pstmt.setString(2, "4");
			pstmt.setString(3, "4");		
			int cnt = pstmt.executeUpdate();			
		}
		long now2 = Calendar.getInstance().getTimeInMillis();
		long ellapse = now2 - now1;
		System.out.println("ellapse: "+ellapse);
		
		pstmt.close();
		conn.close();

	}
	
	
}
