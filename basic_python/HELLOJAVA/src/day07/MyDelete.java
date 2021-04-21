package day07;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Statement;

public class MyDelete {

	public static void main(String[] args) throws Exception {
		

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; //oracle expression(평가판)버전은 xe / 회사에서는 orcl이 대부분
		String sql = "delete sample where col01=?"; //Primary Key는 웬만해선 바꿀 일이 없고, 바꿔서도 안되기 때문에 변경하지 않는게 좋음
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		PreparedStatement pstmt = conn.prepareStatement(sql); //얘는 반복문 돌릴 때 속도가 빠름 
		pstmt.setString(1, "8");
		//index 순서는 오라클 순번을 따름. 1번째부터 시작함. (0번째 없음) 
		//첫번째 변수 값을 3으로 지정. 물음표의 순서
		
		int cnt = pstmt.executeUpdate(); //여기 괄호안에 sql 안들어가게 조심! 이미 위에서 넣어줬음! 
		
		System.out.println("cnt:"+cnt);
		
		
		pstmt.close();
		conn.close();
		

	}
}
