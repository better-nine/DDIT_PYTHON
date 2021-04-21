package day07;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

public class MyPreInsert {
	
	public static void main(String[] args) throws Exception {
		

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; //oracle expression(평가판)버전은 xe / 회사에서는 orcl이 대부분
		String sql = "insert into sample(col01, col02, col03) values(?,?,?)";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		PreparedStatement pstmt = conn.prepareStatement(sql); //얘는 반복문 돌릴 때 속도가 빠름 
		pstmt.setString(1, "9");
		pstmt.setString(2, "9");
		pstmt.setString(3, "9");
		//index 순서는 오라클 순번을 따름. 1번째부터 시작함. (0번째 없음) 
		//첫번째 변수 값을 3으로 지정. 물음표의 순서
		
		int cnt = pstmt.executeUpdate();
		
		System.out.println("cnt:"+cnt);
		
		
		pstmt.close();
		conn.close();
		

	}
	
}
