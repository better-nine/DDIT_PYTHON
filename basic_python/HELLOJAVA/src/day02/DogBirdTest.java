package day02;

public class DogBirdTest {
	public static void main(String[] args) {
		
		Bird b = new Bird();
		
		
		System.out.println(b.power_bark);
		System.out.println(b.power_fly);
		b.exercise(5);
		b.teachFromHuman();
		System.out.println(b.power_bark);
		System.out.println(b.power_fly);
		
		
		
		
		
		
	}
}
