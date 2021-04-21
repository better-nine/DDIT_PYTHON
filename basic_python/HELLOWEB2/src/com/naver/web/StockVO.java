package com.naver.web;

public class StockVO {
	private String s_code;
	private String s_name;
	private String cprice;
	private String in_time;
	
	
	public String getS_code() { //getter setter 변수 앞자리는 대문자로 지정하는게 규약임 
		return s_code; //this 붙여도 되고 안 붙여도 됨 
	}
	public void setS_code(String s_code) {
		this.s_code = s_code;
	}
	public String getS_name() {
		return s_name;
	}
	public void setS_name(String s_name) {
		this.s_name = s_name;
	}
	public String getCprice() {
		return cprice;
	}
	public void setCprice(String cprice) {
		this.cprice = cprice;
	}
	public String getIn_time() {
		return in_time;
	}
	public void setIn_time(String in_time) {
		this.in_time = in_time;
	}
 
	
	
	
	
}
