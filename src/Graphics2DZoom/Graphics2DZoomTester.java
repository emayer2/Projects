package Graphics2DZoom;

import javax.swing.*;
import java.awt.*;

public class Graphics2DZoomTester {
	public static void main(String[] args) {
		// Constructs the GUI skeleton
		JFrame frame = new JFrame("Graphics2DZoom Test Program");
		
		// Creates a face object
		Face f = new Face();
	    f.setPreferredSize(new Dimension(400,400));
	    f.setBackground(Color.cyan);
	    frame.add(f, BorderLayout.CENTER);
	
		frame.pack();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
	}
}