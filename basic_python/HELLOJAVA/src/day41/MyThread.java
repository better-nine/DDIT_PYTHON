package day41;

public class MyThread {
	
	public static void thNum() {
		new Thread(new Runnable() {
			@Override
			public void run() {
				for(int i = 0 ; i < 100000 ; i++) {
					if(i% 100==0) {
						System.out.println();
					}
					System.out.print(i);
				}
			}
		}).start(); //thread는 start를 해야 실행이 됨
	}
	
	public static void thMun() {
		new Thread(new Runnable() {
			@Override
			public void run() {
				for(int i = 0 ; i < 100000 ; i++) {
					if(i% 100==0) {
						System.out.println();
					}
					System.out.print((char)i);
				}
			}
		}).start(); //thread는 start를 해야 실행이 됨
	}
	
	
	public static void main(String[] args) {
		thNum(); 
		thMun(); 
	}
}
