package Graphics2DZoom;

import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;

/**
 * <p>The Graphics2DZoom class allows for easy zooming of the Java awt Graphics2D object,
 * making for easy/convenient zooming, such as zooming to particular positions
 * with a given zoom factor, scaling all zooms by a relative factor, etc.</p>
 * <p>This class is non-static.</p>
 * 
 * @author Ethan Mayer
 */
public class Graphics2DZoom {
	/**
	 * Abstraction Function:
	 * 	relZoom represents the relative scale to zoom to.
	 *	TODO: Update AF as class is written
	 *  
	 * Representation Invariant:
	 * 	No RI since relZoom can be any double.
	 * 	TODO: Update RI as class is written
	 */

	// Zoom members
	private double relZoom;   // Relative scale to zoom to

	/**
	 * Creates a new Graphics2DZoom object, with a relative zoom of 1.0
	 */
	public Graphics2DZoom() {
		this(1.0);
	}

	/**
	 * Creates a new Graphics2DZoom object with a relative zoom of
	 * the passed parameter relativeZoom.
	 * @param relativeZoom - the relative zoom of this
	 */
	public Graphics2DZoom(double relativeZoom) {
		this.relZoom = relativeZoom;
	}


	/**
	 * Zooms in the passed Graphics2D object to the given scale (zoomX, zoomY)
	 * and passed location (x, y), zooming to the the current relative zoom factor.
	 * (x,y) will be zoomed to the location of the middle of the window
	 * with the passed width by height.
	 * @param g - Graphics2D object to zoom
	 * @param x - x position to zoom to
	 * @param y - y position to zoom to
	 * @param zoomX - x zoom scale, relative to absolute zoom scale
	 * @param zoomY - y zoom scale, relative to absolute zoom scale
	 * @param width - width of the drawing area
	 * @param height - height of the drawing area
	 * @modifies g
	 * @effects the zoom and focal position of g
	 * @throws IllegalArgumentException if g is null
	 */
	public void zoom(Graphics2D g,
			 		 double x, double y,
			 		 double zoomX, double zoomY,
			 		 double width, double height) {
		if (g == null) {
			// g was null, throw an IllegalArgumentException
			System.err.println("Graphics2D parameter g must be non-null.");
			throw new IllegalArgumentException();
		}
		
		// Finds the x, y, and zoom of the current
		AffineTransform tr = g.getTransform();
		double xPos = tr.getTranslateX();   // x position of current zoom
		double yPos = tr.getTranslateY();   // y position of current zoom
		double currZoomX = tr.getScaleX();  // Current x zoom factor
		double currZoomY = tr.getScaleY();  // Current y zoom factor

		// Un-zooms and un-translates from the current position
		g.scale(1.0 / currZoomX, 1.0 / currZoomY);
		g.translate(xPos, yPos);

		// Shifts and zooms to the new location
		double totZoomX = zoomX * relZoom;
		double totZoomY = zoomY * relZoom;
		
		g.translate(-(x - (width / (2.0 * totZoomX))) * totZoomX,
					-(y - (height / (2.0 * totZoomY))) * totZoomY);
		g.scale(totZoomX, totZoomY);
	}

	/**
	 * Zooms in the passed Graphics2D object to the given scale (zoom),
	 * for both x and y, and passed location (x, y), 
	 * zooming to the the current relative zoom factor.
	 * (x,y) will be zoomed to the location of the middle of the window
	 * with the passed width by height.
	 * @param g - Graphics2D object to zoom
	 * @param x - x position to zoom to
	 * @param y - y position to zoom to
	 * @param zoom - zoom scale, relative to absolute zoom scale
	 * @param width - width of the drawing area
	 * @param height - height of the drawing area
	 * @modifies g
	 * @effects the zoom and focal position of g
	 * @throws IllegalArgumentException if g is null
	 */
	public void zoom(Graphics2D g,
					 double x, double y,
					 double zoom,
					 double width,
					 double height) {
		zoom(g, x, y, zoom, zoom, width, height);
	}

	/**
	 * Returns the current absolute (relative) zoom scale.
	 * @returns the double value of the current absolute zoom scale
	 */
	public double getAbsZoom() {
		return relZoom;
	}

	/**
	 * Sets the current absolute (relative) zoom scale.
	 * @param newScale - the new value of the current absolute zoom scale
	 */
	public void setAbsZoom(double newScale) {
		this.relZoom = newScale;
	}
}





