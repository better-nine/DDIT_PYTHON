package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyGui04 extends JFrame {

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
					MyGui04 frame = new MyGui04();
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
	public MyGui04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setText("1");
		tf1.setBounds(36, 96, 116, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setText("2");
		tf2.setBounds(49, 148, 116, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String tf11 = tf1.getText();
				String tf22 = tf2.getText();
				
				int tf111 = Integer.parseInt(tf11);
				int tf222 = Integer.parseInt(tf22);
				
				int result = tf111 + tf222;
				tf3.setText(String.valueOf(result));
				
				
				
			}
		});
		btn.setBounds(85, 179, 97, 23);
		contentPane.add(btn);
		
		JLabel lbl = new JLabel("+");
		lbl.setBounds(119, 123, 57, 15);
		contentPane.add(lbl);
		
		tf3 = new JTextField();
		tf3.setBounds(147, 212, 116, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
	}

}
