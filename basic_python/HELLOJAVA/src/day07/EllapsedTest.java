package day07;

import java.util.Calendar;

public class EllapsedTest {
	public static void main(String[] args) {
		
		
		long now1 = Calendar.getInstance().getTimeInMillis();

		long now2 = Calendar.getInstance().getTimeInMillis();
		
		long ellapse = now2 - now1;
		
		System.out.println(ellapse);
		// 글씨가 작으니깐 좀 키워주자
		
		
		
		
		
	}	
}
