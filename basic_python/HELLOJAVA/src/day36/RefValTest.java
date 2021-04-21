package day36;

public class RefValTest {
	
	
	public static void changeA(String a) {
		a = "8";
	}

	public static void changeArr(String[] arr) {
		arr[0] = "8";
	}
	
	public static void main(String[] args) {
		
		String a = "7";
		String[] arr = {"7"};
		
		System.out.println("a : "+a);
		System.out.println("arr : "+arr[0]);
		
		changeA(a);
		changeArr(arr);
		
		System.out.println("a : "+a);
		System.out.println("arr : "+arr[0]);
		
		
		
		
		
		
	}
}
