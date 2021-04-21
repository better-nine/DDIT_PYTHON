package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyGui06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				
				try {
					MyGui06 frame = new MyGui06();
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
	public MyGui06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setText("1");
		tf1.setBounds(0, 38, 116, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setText("10");
		tf2.setBounds(173, 38, 116, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		JLabel lbl = new JLabel("에서");
		lbl.setBounds(128, 41, 57, 15);
		contentPane.add(lbl);
		
		tf3 = new JTextField();
		tf3.setBounds(276, 89, 116, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
		
		JButton btn = new JButton("까지 합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				int a = Integer.parseInt(tf1.getText());
				int b = Integer.parseInt(tf2.getText());

				for(int i = a+1 ; i < b+1 ; i++) {
					a += i;
				}
				
				tf3.setText(String.valueOf(a));

				//이렇게 해도 됨 미리 결과값 넣을 result 선언하고 하기 
//				int result = 0;
//				for(int i = a ; i < b ; i++) {
//				result += i;
				
			}
		});
		btn.setBounds(302, 37, 97, 23);
		contentPane.add(btn);
	}

}
