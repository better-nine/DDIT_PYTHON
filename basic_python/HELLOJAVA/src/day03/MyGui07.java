package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyGui07 extends JFrame {

	private JPanel contentPane;
	JTextArea ta;
//	String count = "";

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyGui07 frame = new MyGui07();
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
	public MyGui07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				JButton temp = (JButton)e.getSource(); //내가 누른 버튼이 어떤 값을 가지고 있는지 알려줌 
//				temp.getText(); //버튼이 가지고 있는 text의 값이 나옴 
				
				myclick(e);
				
//				//2단을 출력해야함 2*1 = 2
//				String count = "";
//				int b2 = Integer.parseInt(btn2.getText());
//				for(int i = 1 ; i<10 ; i++) {
//					count += b2 + "*" + i + "=" + b2*i + "\n";
//					ta.setText(count);
//				
//				}
////				++i;
				
				
			}
		});
		
		btn2.setBounds(226, 10, 97, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String count = "";
				int b3 = Integer.parseInt(btn3.getText());
				for(int i = 1 ; i<10 ; i++) {
					count += b3 + "*" + i + "=" + b3*i + "\n";
					ta.setText(count);
				
				}
			}
		});
		btn3.setBounds(226, 35, 97, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String count = "";
				int b4 = Integer.parseInt(btn4.getText());
				for(int i = 1 ; i<10 ; i++) {
					count += b4 + "*" + i + "=" + b4*i + "\n";
					ta.setText(count);
				
				}
			}
		});
		btn4.setBounds(226, 60, 97, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String count = "";
				int b5 = Integer.parseInt(btn5.getText());
				for(int i = 1 ; i<10 ; i++) {
					count += b5 + "*" + i + "=" + b5*i + "\n";
					ta.setText(count);
				
				}
			}
		});
		btn5.setBounds(226, 85, 97, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String count = "";
				int b6 = Integer.parseInt(btn6.getText());
				for(int i = 1 ; i<10 ; i++) {
					count += b6 + "*" + i + "=" + b6*i + "\n";
					ta.setText(count);
				
				}
			}
		});
		btn6.setBounds(226, 109, 97, 23);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String count = "";
				int b7 = Integer.parseInt(btn7.getText());
				for(int i = 1 ; i<10 ; i++) {
					count += b7 + "*" + i + "=" + b7*i + "\n";
					ta.setText(count);
				
				}
			}
		});
		btn7.setBounds(226, 142, 97, 23);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String count = "";
				int b8 = Integer.parseInt(btn8.getText());
				for(int i = 1 ; i<10 ; i++) {
					count += b8 + "*" + i + "=" + b8*i + "\n";
					ta.setText(count);
				
				}
			}
		});
		btn8.setBounds(226, 175, 97, 23);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String count = "";
				int b9 = Integer.parseInt(btn9.getText());
				for(int i = 1 ; i<10 ; i++) {
					count += b9 + "*" + i + "=" + b9*i + "\n";
					ta.setText(count);
				
				}
			}
		});
		btn9.setBounds(226, 208, 97, 23);
		contentPane.add(btn9);
		
		ta = new JTextArea();
		ta.setBounds(12, 9, 186, 242);
		contentPane.add(ta);
	}
	
	
	public void myclick(MouseEvent e) {
		int dan = Integer.parseInt(((JButton)e.getSource()).getText());
		
		String text = "";
		
		text += dan+"*"+1+"="+(dan*1)+"\n";
		text += dan+"*"+2+"="+(dan*2)+"\n";
		text += dan+"*"+3+"="+(dan*3)+"\n";
                                     
		text += dan+"*"+4+"="+(dan*4)+"\n";
		text += dan+"*"+5+"="+(dan*5)+"\n";
		text += dan+"*"+6+"="+(dan*6)+"\n";
		                             
		text += dan+"*"+7+"="+(dan*7)+"\n";
		text += dan+"*"+8+"="+(dan*8)+"\n";
		text += dan+"*"+9+"="+(dan*9)+"\n";
		
		ta.setText(text);
		
	}
		
	
	
}
