package day41;

public class MyMethod {
	public static void showNum() {
		for(int i = 0 ; i < 100000 ; i++) {
			if(i% 100==0) {
				System.out.println(" ");
			}
			System.out.print(i);
		}
	}
	
	public static void showMun() {
		for(int i = 0 ; i < 100000 ; i++) {
			if(i% 100==0) {
				System.out.println(" ");
			}
			System.out.print((char)i);
		}
	}
	
	public static void main(String[] args) {
		showNum();
		showMun();
		
	}
}
