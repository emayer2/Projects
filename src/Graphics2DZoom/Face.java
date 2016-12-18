package Graphics2DZoom;

import java.awt.*;
import javax.swing.*;


/**
 * Basic Java graphics demo: JPanel with a face drawn in it. 
 * CSE 331 12au-16au.  Based on old intro course examples.
 * 
 * @author Hal Perkins, Ethan Mayer
 */
@SuppressWarnings("serial")
public class Face extends JPanel {
	private final double ZOOM_STEP = 0.001;
	private Graphics2DZoom gzoom = new Graphics2DZoom(1.0);
	private ZoomTransition tr = new ZoomTransition(1.0, 2.0, ZOOM_STEP);


	/** Paint a smiley face/grid centered in this JPanel **/
	@Override
	public void paintComponent(Graphics g) {
		Graphics2D g2 = (Graphics2D) g;
		// Note: The drawing code here uses the old AWT procedural interface to 
		// draw shapes.  A version taking full advantage of Graphics2D would
		// create actual shape objects and add them to the picture.

		// paint background
		super.paintComponent(g);

		// get width and height of drawing area
		int height = getHeight();
		int width  = getWidth();

		// Zooms to the midpoint, 2x zoom
		double currZoom = tr.getZoom();
		tr.step();
		gzoom.zoom(g2, 
				   width/2.0,// * (currZoom - 1.0) / (zoom - 1.0),
				   height/2.0,// * (currZoom - 1.0) / (zoom - 1.0), 
				   currZoom, width, height);
		
		// Draws a grid
		for (int i = 0; i < height/10 + 1; i++) {
			g2.setColor(new Color(i/(float)(height/10 + 1), i/(float)(height/10 + 1), i/(float)(height/10 + 1)));
			g2.drawLine(0, i*10, width, i*10);
			for (int j = 0; j < width/10 + 1; j++) {
				g2.setColor(new Color(j/(float)(width/10 + 1), j/(float)(width/10 + 1), j/(float)(width/10 + 1)));
				g2.drawLine(j*10, 0, j*10, height);
			}
		}

		// draw face that takes up 80% of the JPanel
		int faceTop  = height/10;
		int faceLeft = width/10;
		int faceHeight = height - height/5;
		int faceWidth  = width  - width/5;

		// outline
		g2.setColor(Color.yellow);
		g2.fillOval(faceLeft, faceTop, faceWidth, faceHeight);

		// eyes
		g2.setColor(Color.black);
		g2.fillOval(faceLeft+(int)(width*0.2), faceTop+(int)(height*0.2),
				width/10, height/10);
		g2.fillOval(faceLeft+(int)(width*0.5), faceTop+(int)(height*0.2),
				width/10, height/10);

		// nose
		Polygon nose = new Polygon();
		nose.addPoint(faceLeft+(int)(width*0.40), faceTop+(int)(height*0.35));
		nose.addPoint(faceLeft+(int)(width*0.45), faceTop+(int)(height*0.50));
		nose.addPoint(faceLeft+(int)(width*0.35), faceTop+(int)(height*0.50));
		g2.fillPolygon(nose);

		// mouth
		g2.fillArc(faceLeft+(int)(width*0.25), faceTop+(int)(height*0.5),
				(int)(width*0.3), (int)(height*0.2),
				0, -180);

		if (tr.isFinished() && tr.getEnd() == 2.0) {
			tr = new ZoomTransition(2.0, 1.0, ZOOM_STEP);
		} else if (tr.isFinished() && tr.getEnd() == 1.0) {
			tr = new ZoomTransition(1.0, 2.0, ZOOM_STEP);
		}
		
		this.repaint();
	}
}