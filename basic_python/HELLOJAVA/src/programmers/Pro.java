package programmers;

public class Pro {
	public static void main(String[] args) {
		
		Pro p = new Pro();
		boolean aaa = p.solution("123123");
		
		System.out.println(aaa);
		
	}
	
	public boolean solution(String s) {
		
		boolean answer = true;

		String[] sl = s.split("");
		
		if(sl.length == 4 || sl.length == 6) {
			for(int i = 0; i<sl.length; i++) {
		    	try {
		    		int num = Integer.parseInt(sl[i]);	    		
		    		continue;
		    	} catch (Exception e) {
		    		answer = false;
		    		break;
		    	}
		    }
			return answer;
		} else {
			answer = false;
			return answer;
		}
	}

	
	
	
	
	
	
	
	//전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
	//여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
	public int solution2(int n, int[] lost, int[] reserve) {
		int have = reserve.length;
		int answer = 0;
		int jungbok = 0;
		//lost에 있는 값이 reserve에 있을 경우 빌려줄 수 없음
		//lost에 있는 값이 reserve에 있을 경우 +0
		for(int j = 0 ; j < reserve.length ; j++) { //여벌이 있는 학생 수 만큼 회전			
			for(int i = 0 ; i < lost.length ; i++) { //잃어버린 학생의 수만큼 회전							
				if(reserve[j]==lost[i]) {
					jungbok += 1;
					break;		//lost에 있는 값이 reserve에 있을 경우 빌려줄 수 없음
				} else if (reserve[j]-1==lost[i]){ //앞번호 친구가 갖고있을 경우
					answer += 1;
					break;		
				} else if (reserve[j]+1==lost[i]) { //뒷번호 친구가 갖고있을 경우
					answer += 1;
					break;							
				} else { //아무도 없음 
					break;
				}
			}			
		}
		
		
		int student = (lost.length + reserve.length) - jungbok;
		
		
		//reserve에 들어있고, lost보다 1이 크거나 작으면 빌려줄 수 있음
		//reserve에 들어있고, reserve[i]+1==lost[j]||reserve[i]-1==lost[j]   +1
		
		return answer+student;
	}
	
/*	
	
	
	
	 //전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
	//여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
	public int solution2(int n, int[] lost, int[] reserve) {
		int have = reserve.length;
		int answer = 0;
		for(int i = 0 ; i < lost.length ; i++) {
			for(int j = 0 ; j < reserve.length ; j++) {
				if(lost[i]==reserve[j]) { //도난당한 친구가 여벌이 있을 경우 
					break;
				}
				if(lost[i]==reserve[j]-1||lost[i]==reserve[j]+1) { //도난당한 친구 앞뒤에 여벌이 없을 경우 
					break;
				}
				if(lost[i]+1==reserve[j]||lost[i]-1==reserve[j]) { //도난당한 친구 앞뒤에 여벌이 존재할경우
					answer += 1;
					break;
				} 				
			}
			break;
		}  
	    return answer+have;
	 }
*/	
	
	
	
	
	
	
	
}
