package programmers;

public class P0323_2 {
	public static void main(String[] args) {
		
		String a1 = "1S2D*3T";
 
		int aaa = solution(a1);
		
		
	}
	public static int solution(String dartResult) {
		
		String[] dartResult_arr = dartResult.split("");
		
		int score = 0;
		int acha = 0;
		
		for (int i = 0 ; i < dartResult_arr.length ; i++ ) {
			
			System.out.println(dartResult_arr[i]);
			int temp_score = 0;
			
			if(dartResult_arr[i].equals("S")) {
				temp_score = Integer.parseInt(dartResult_arr[i-1]);
				System.out.println("S" + temp_score);

			} else if (dartResult_arr[i].equals("D")) {
				int temp = Integer.parseInt(dartResult_arr[i-1]);
				temp_score = (int) Math.pow(temp, 2);
				System.out.println("D" + temp_score); //여기서 터진다잉 
					
			} else if (dartResult_arr[i].equals("T")) {
				int temp = Integer.parseInt(dartResult_arr[i-1]);
				temp_score = (int) Math.pow(temp, 3);
				System.out.println("T" + temp_score);

			} else if (dartResult_arr[i].equals("*")) {
				int temp = Integer.parseInt(dartResult_arr[i-1]);
				temp_score = score * 2;
					//만약 세번째 점수라면 첫번째 점수 빼야함 
				System.out.println("*" + temp_score);
					
			} else if (dartResult_arr[i].equals("#")) {
				acha += Integer.parseInt(dartResult_arr[i-2]);
				System.out.println("#");
			} else {
				System.out.println("?????????????");
				
			}
			score += temp_score;
			
		}
		score = score - acha;
        return score;
    }
	
}
