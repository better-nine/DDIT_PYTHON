package day09;

public class MyThread02 {
	
	public static void showText() {
		new Thread(new Runnable() {//스레드를 호출하면 run안이 동작함
			@Override
			public void run() {
				for(int i = 0; i <= 100000 ; i++) {
					System.out.print((char)i + " "); //숫자에 해당하는 아스키값으로 캐스팅가능
					if(i%100==0) {
						System.out.println();
					}
				}				
			}
		}).start();
	}
	
	public static void showNum() {
		new Thread(new Runnable() {//스레드를 호출하면 run안이 동작함
			@Override
			public void run() {
				for(int i = 0; i <= 100000 ; i++) {
					System.out.print(i + " "); //숫자에 해당하는 아스키값으로 캐스팅가능
					if(i%100==0) {
						System.out.println();
					}
				}				
			}
		}).start();	
	}
	
	
	
	public static void main(String[] args) {
		showNum();
		showText();
		
	}
	
	
	
}
