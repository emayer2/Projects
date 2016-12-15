package GraphicsZoom;

import java.awt.Graphics2D;

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
	private double relZoom;  // Relative scale to zoom to
	
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
	 * Zooms in the passed Graphics2D object to the given scale (zoom)
	 * and passed location (x, y), zooming to the the current relative zoom factor.
	 * @param g - Graphics2D object to zoom
	 * @param x - x position to zoom to
	 * @param y - y position to zoom to
	 * @param zoom - zoom scale, relative to absolute zoom scale
	 * @modifies g
	 * @effects the zoom and focal position of g
	 * @throws IllegalArgumentException if g is null
	 */
	public void zoom(Graphics2D g, double x, double y, double zoom) {
		try {
			// Shifts the to appropriate location, and zooms
			g.translate(x, y);
			g.scale(zoom * relZoom, zoom * relZoom);
		} catch (NullPointerException e) {
			// g was null, throw an IllegalArgumentException
			System.err.println("Graphics2D parameter g must be non-null.");
			e.printStackTrace();
			throw new IllegalArgumentException();
		}
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






