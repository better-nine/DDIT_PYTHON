package kr.aimaker.mybatis;

import java.util.List;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

public class SampleDAO {
	private SqlSessionFactory sqlSessionFactory = null;

	public SampleDAO(SqlSessionFactory sqlSessionFactory) {
		this.sqlSessionFactory = sqlSessionFactory;
	}
	
	public List myselect(SampleVO vo) {
		List list = null;
		SqlSession session = sqlSessionFactory.openSession();

		try {
			list = session.selectList("sample.selectList", vo);
		} finally {
			session.close();
		}
		return list;
	}
	
	public int myinsert(SampleVO vo) {
		int cnt = -1;
		SqlSession session = sqlSessionFactory.openSession();
		
		try {
			cnt = session.update("sample.insert", vo);
		} finally {
			session.commit();
			session.close();
		}
		return cnt;
	}
	
	public int myupdate(SampleVO vo) {
		int cnt = -1;
		SqlSession session = sqlSessionFactory.openSession();
		
		try {
			cnt = session.update("sample.update", vo);
		} 
		finally {
			session.commit();
			session.close();
		}
		return cnt;
	}
	
	public int mydelete(SampleVO vo) {
		int cnt = -1;
		SqlSession session = sqlSessionFactory.openSession();
		
		try {
			cnt = session.update("sample.delete", vo);
		} 
		finally {
			session.commit();
			session.close();
		}
		return cnt;
	}

	public static void main(String[] args) {
		
		SampleDAO dao = new SampleDAO(MyBatisConnectionFactory.getSqlSessionFactory());
		
		SampleVO vo = new SampleVO();
		vo.setCol01("3");		
		vo.setCol02("5");		
		vo.setCol03("5");		
		
		int cnt = dao.mydelete(vo);
		System.out.println(cnt);
		
		
//		SampleVO vo = new SampleVO();
//		vo.setCol01("3");		
//		vo.setCol02("5");		
//		vo.setCol03("5");		
//		
//		int cnt = dao.myupdate(vo);
//		System.out.println(cnt);
		
//		SampleVO vo = new SampleVO();
//		vo.setCol01("3");		
//		vo.setCol02("3");		
//		vo.setCol03("3");		
//		
//		int cnt = dao.myinsert(vo);
//		System.out.println(cnt);
		
		
//		SampleVO vo = new SampleVO();
//		vo.setCol01("1");		
//		List<SampleVO> list = dao.myselect(vo);
//		System.out.println(list.size());
	}

}





