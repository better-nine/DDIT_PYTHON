package programmers;

import java.util.Scanner;

public class P0323 {
	
	public static String solu(int a, int b) {
		int month = 0;
		int date = 0;
		String answer = null;
  
		if(a==1 || a==4 || a==7) { //금
			date = b % 7;
		} else if(a==2 || a==8) { //월
			date = (b+3) % 7;
		} else if(a==3 || a==11) { //화
			date = (b+4) % 7;
		} else if(a==9 || a==12) { //목
			date = (b+6) % 7;
		} else if(a==10) { //토
			date = (b+1) % 7;
		} else if(a==5) { //일
			date = (b+2) % 7;
		} else if(a==6) { //수
			date = (b+5) % 7;
		} 
		
		switch( date ) {
			case 0: //목
				answer = "THU";
				return answer;
			case 1: //금
				answer = "FRI";
				return answer;
			case 2: //토
				answer = "SAT";
				return answer;
			case 3: //일
				answer = "SUN";
				return answer;
			case 4: //월
				answer = "MON";
				return answer;
			case 5: //화
				answer = "TUE";
				return answer;
			case 6: //수
				answer = "WED";
				return answer;
		}
		System.out.println(a);
		System.out.println(date);
		
		System.out.println(answer);
		return answer;
		
	}
	
	public static void main(String[] args) {
		
		String a =  solu(5,24);
		System.out.println(a);	
		
		int b = 24 % 7;
		System.out.println(b);
		
	}
}
