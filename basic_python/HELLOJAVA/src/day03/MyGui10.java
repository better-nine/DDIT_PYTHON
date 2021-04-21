package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.Popup;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.AbstractAction;
import java.awt.event.ActionEvent;
import javax.swing.Action;
import static javax.swing.JOptionPane.showMessageDialog;
import java.awt.event.ActionListener;
import javax.swing.SwingConstants;

public class MyGui10 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	String number = "";

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyGui10 frame = new MyGui10();
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
	public MyGui10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.CENTER);
		tf.setBounds(45, 23, 313, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				
//				myclick(e); //얘만 호출하면 다른데서도 다 부를 수 있음 
				//여러개가 같은곳에 적용되는 경우에는 메서드를 생성해서 활용하는게 훨씬 더 합리적인듯 
				
//				
				number += btn1.getText();
				tf.setText(number);
				
			}
		});
		btn1.setBounds(45, 74, 97, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				number += btn2.getText();
				tf.setText(number);
			}
		});
		btn2.setBounds(154, 74, 97, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				number += btn3.getText();
				tf.setText(number);
			}
		});
		btn3.setBounds(261, 74, 97, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				number += btn4.getText();
				tf.setText(number);
				
			}
		});
		btn4.setBounds(45, 109, 97, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				number += btn5.getText();
				tf.setText(number);
				
			}
		});
		btn5.setBounds(154, 109, 97, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				number += btn6.getText();
				tf.setText(number);
				
			}
		});
		btn6.setBounds(261, 109, 97, 23);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				number += btn7.getText();
				tf.setText(number);
				
			}
		});
		btn7.setBounds(45, 148, 97, 23);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				number += btn8.getText();
				tf.setText(number);
				
			}
		});
		btn8.setBounds(154, 148, 97, 23);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				number += btn9.getText();
				tf.setText(number);
				
			}
		});
		btn9.setBounds(261, 148, 97, 23);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				number += btn0.getText();
				tf.setText(number);
				
			}
		});
		btn0.setBounds(154, 189, 97, 23);
		contentPane.add(btn0);
		
		JButton btn_call = new JButton("CALL");
		btn_call.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn_call.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				showMessageDialog(btn_call, number);
				
			}
		});
		btn_call.setBounds(261, 189, 97, 23);
		contentPane.add(btn_call);
	}



	public void myclick(MouseEvent e) {
		JButton temp = (JButton)e.getSource();
		String text = temp.getText();
		
		String old_num = tf.getText();
		
		tf.setText(old_num+text);
		
	}
	
	public void myPopUp() {
		String msg = "calling" + tf.getText();
		JOptionPane.showMessageDialog(null, msg);
	}
	
	
}
