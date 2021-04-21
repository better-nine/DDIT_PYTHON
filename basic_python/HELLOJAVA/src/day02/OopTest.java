package day02;

public class OopTest {
	public static void main(String[] args) {
		
		Animal ani = new Animal();
		
		System.out.println(ani.age);
		ani.getOld();
		System.out.println(ani.age);
		System.out.println("--------------------------");
		
		
		Human hum = new Human();
		
		System.out.println(hum.age);
		System.out.println(hum.power_lang);
		System.out.println("--------------------------");
		hum.getOld();
		hum.learn_lang();
		System.out.println(hum.age);
		System.out.println(hum.power_lang);
		System.out.println("--------------------------");		
		hum.kwawe(5);
		System.out.println(hum.age);
		System.out.println(hum.power_lang);
		System.out.println("--------------------------");
		
		
		
		
	}
}

