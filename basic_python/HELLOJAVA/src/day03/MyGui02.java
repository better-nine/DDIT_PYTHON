package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyGui02 extends JFrame {

	private JPanel contentPane;
	JLabel lbl;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyGui02 frame = new MyGui02();
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
	public MyGui02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl = new JLabel("1");
		lbl.setBounds(68, 124, 57, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("Increase");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				
			
				
				String s = lbl.getText();
				//갈색은 지역변수 파란색은 전역변수
				
				int a = Integer.parseInt(s);
				++a;
				lbl.setText(a+"");
					
//				Integer.toString(a);
//				Integer.parseInt(s);
				//형변환하는거 기억하기~~~~~~~~~~
				
			}
		});
		btn.setBounds(234, 120, 97, 23);
		contentPane.add(btn);
	}

}
