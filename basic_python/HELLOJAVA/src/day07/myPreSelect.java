package day07;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.ResultSet;  
import java.sql.Statement;


public class myPreSelect {
		
	public static void main(String[] args) throws Exception {
		

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; //oracle expression(평가판)버전은 xe / 회사에서는 orcl이 대부분
		String sql = "select col01, col02, col03 from sample where col01=?";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		PreparedStatement pstmt = conn.prepareStatement(sql); //얘는 반복문 돌릴 때 속도가 빠름 
		pstmt.setString(1, "3");
		//index 순서는 오라클 순번을 따름. 1번째부터 시작함. (0번째 없음) 
		//첫번째 변수 값을 3으로 지정. 물음표의 순서
		
		ResultSet rs = pstmt.executeQuery();
		
		//rs.next() : 뒤에 데이터가 있는지 여부를 물음
		
		
		while (rs.next()) {
			String col01 = rs.getString("col01");
			String col02 = rs.getString("col02");
			String col03 = rs.getString("col03");
			
			System.out.print("col01 : "+ col01);
			System.out.print(" col02 : "+ col02);
			System.out.println(" col03 : "+ col03);
		}
		
		pstmt.close();
		conn.close();
		

	}
}
