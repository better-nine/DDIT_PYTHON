package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyGui08 extends JFrame {

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
					MyGui08 frame = new MyGui08();
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
	public MyGui08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JButton btn = new JButton("결과");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
//				tf_mine tf_com = tf_result
				
				
				String tfm = tf_mine.getText();

				int comresult = (int)(Math.random()*2);
				
				if(comresult==0) {
					tf_com.setText("홀");
				} else {
					tf_com.setText("짝");
				}
				
				if(tfm.equals(tf_com.getText())) {
					tf_result.setText("이김");
				} else {
					tf_result.setText("짐");
				}
				
				
			}
		});
		btn.setBounds(12, 178, 97, 23);
		contentPane.add(btn);
		
		lbl1 = new JLabel("MINE");
		lbl1.setBounds(29, 96, 57, 15);
		contentPane.add(lbl1);
		
		tf_mine = new JTextField();
		tf_mine.setBounds(143, 93, 116, 21);
		contentPane.add(tf_mine);
		tf_mine.setColumns(10);
		
		tf_com = new JTextField();
		tf_com.setBounds(143, 124, 116, 21);
		contentPane.add(tf_com);
		tf_com.setColumns(10);
		
		lbl2 = new JLabel("COMPUTER");
		lbl2.setBounds(29, 127, 97, 15);
		contentPane.add(lbl2);
		
		tf_result = new JTextField();
		tf_result.setBounds(143, 179, 116, 21);
		contentPane.add(tf_result);
		tf_result.setColumns(10);
	}

}
