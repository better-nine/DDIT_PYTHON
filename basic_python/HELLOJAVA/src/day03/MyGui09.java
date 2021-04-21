package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JTextField;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyGui09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_mine;
	private JTextField tf_com;
	private JTextField tf_result;
	JLabel lbl1;
	JLabel lbl2;
	

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyGui09 frame = new MyGui09();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyGui09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl1 = new JLabel("Mine");
		lbl1.setBounds(12, 58, 57, 15);
		contentPane.add(lbl1);
		
		lbl2 = new JLabel("Computer");
		lbl2.setBounds(12, 103, 57, 15);
		contentPane.add(lbl2);
		
		JButton btn = new JButton("result");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				int comrandom = (int)(Math.random()*3);
				//컴퓨터 랜덤 숫자 0 1 2
				
				
				String com = "";
				String result ="";

				if(comrandom==0) {
					com = "가위";
				} else if(comrandom==1) {
					com = "바위";
				} else { //2
					com = "보";
				}
				
				String mine = tf_mine.getText(); //내거 가져온거임 
				
				if(mine.equals(com)) {
					result = "비김";
				} else if(mine.equals("가위")&&com.equals("바위")||mine.equals("바위")&&com.equals("보")||mine.equals("보")&&com.equals("가위")) {
					result = "짐";
				} else if(mine.equals("바위")&&com.equals("가위")||mine.equals("보")&&com.equals("바위")||mine.equals("가위")&&com.equals("보")) {
					result = "이김";					
				}
				
				tf_com.setText(com);
				tf_result.setText(result);
				
				
				
				
				
			}
		});
		btn.setBounds(12, 149, 97, 23);
		contentPane.add(btn);
		
		tf_mine = new JTextField();
		tf_mine.setBounds(152, 55, 116, 21);
		contentPane.add(tf_mine);
		tf_mine.setColumns(10);
		
		tf_com = new JTextField();
		tf_com.setBounds(152, 100, 116, 21);
		contentPane.add(tf_com);
		tf_com.setColumns(10);
		
		tf_result = new JTextField();
		tf_result.setBounds(152, 150, 116, 21);
		contentPane.add(tf_result);
		tf_result.setColumns(10);
		
		JLabel lblNewLabel = new JLabel("가위바위보");
		lblNewLabel.setBounds(94, 10, 174, 15);
		contentPane.add(lblNewLabel);
	}

}
