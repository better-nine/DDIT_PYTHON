package net.ivyro.naeun;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class Temp1DAO {
	
	
	
	public int myinsert(String jdata) throws Exception {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe"; 	
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(jdata);
		 
		stmt.close();
		conn.close();
		 
		return cnt;
	}
	
			//자료뭉치 여러개를 넣어서 반환할거라 리턴값은 arraylist
			//자료뭉치 객체 타입은 temp1VO 클래스
	public ArrayList<Temp1VO> myselect() throws Exception{ //전부 다 가져올거기 때문에 매개변수는 안넣음
		
		ArrayList<Temp1VO> list = new ArrayList<Temp1VO>();
		
		//데이터베이스에서 데이터를 가져오기 위해 driver클래스를 로드하기
		String driver = "oracle.jdbc.driver.OracleDriver"; 
		Class.forName(driver); //여기서 Exception 경고 뜨는데 throws로 던졌음
		
		//그 다음 데이터베이스와 연결되는 객체를 가져올거임 
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		//Connection,DriverManager <-얘네 import 할 때 java.sql로 import 해야함 
		Connection con = DriverManager.getConnection(url, "python", "python");
	
		//그리고 sql문장을 실행할 수 있는 객체를 만들거임
		String sql = "select user_id, user_name, user_pass from temp1";
		//Statement도 import할 때 java.sql로 해야함
		Statement stmt = con.createStatement(); //parameter없는 SQL 문은 일반적으로 Statement 객체를 사용
		
		//결과값을 저장할 객체임 결과값뭉치가 들어있다고 생각하면 될듯
		ResultSet rs = stmt.executeQuery(sql); //select문 사용할 때는 executeQuery(parameter) 사용함
		
		//rs는 처음에 컬럼명 라인에 위치해 있다고 가정하기 때문에
		//처음 무조건 한번은 next()를 사용해서 다음 row로 넘겨줘야 첫번째 row에 있는 값이 나옴 
		while (rs.next()) {
			//getString()를 사용해서 컬럼번호 또는 컬럼명을 통해
			//rs의 커서가 위치한 row에 해당하는 값을 구할 수 있음
			String uid = rs.getString("user_id"); //user_id 대신 컬럼번호도 가능함 
			String ups = rs.getString("user_pass");
			String unm = rs.getString("user_name");
	
			//그리고 위에서 뽑아낸 값을 임시로 저장해줄 객체VO를 만들고 저장한 다음
			Temp1VO tempvo = new Temp1VO();
			tempvo.setUser_id(uid);
			tempvo.setUser_pass(ups);
			tempvo.setUser_name(unm);
			list.add(tempvo); //리스트에 추가해서 마지막에 이 친구를 리턴해줌
			
		}
		
		//그리고 데이터 추출이 다 끝나고 나면 연결을 끊어줘야함 
		
		stmt.close();
		con.close();
		
		return list;
	}

	public static void main(String[] args) {
		
		Temp1DAO dao = new Temp1DAO();
		
		ArrayList<Temp1VO> list = null;
		
		
		try {
			list = dao.myselect();
		} catch (Exception e) {
			System.out.println(e);
		}

		System.out.println(list.size());
		
		for(int i = 0 ; i < list.size() ; i++) {
			Temp1VO vo = list.get(i);
			
			String u1 = vo.getUser_id();
			String u2 = vo.getUser_pass();
			String u3 = vo.getUser_name();
			
			System.out.println(u1 + u2 + u3);
			
			
		}
		
		
		
		
		
	}
	
	
	
}
