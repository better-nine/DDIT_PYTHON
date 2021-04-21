package day09;

public class MyThread01 {
	
	public static void showText() {
		for(int i = 0; i <= 100000 ; i++) {
			System.out.print((char)i); //숫자에 해당하는 아스키값으로 캐스팅가능
			if(i%100==0) {
				System.out.println();
			}
		}
	}
	
	public static void showNum() {
		
		for(int i = 0; i <= 100000 ; i++) {
			System.out.print(i);
			if(i%100==0) {
				System.out.println();
			}
			
		}
		
	}
	
	
	
	public static void main(String[] args) {
		showText();
		
	}
	
	
	
}
