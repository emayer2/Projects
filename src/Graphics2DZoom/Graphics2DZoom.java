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
	 * 	relZoomX represents the relative scale to zoom to for x.
	 *  relZoomY represents the relative scale to zoom to for y.
	 *	TODO: Update AF as class is written
	 *  
	 * Representation Invariant:
	 * 	No RI since relZoomX, relZoomY can be any double.
	 * 	TODO: Update RI as class is written
	 */

	// Zoom members
	private double relZoomX;  // Relative scale to zoom to for y
	private double relZoomY;  // Relative scale to zoom to for x

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
		this.relZoomX = relativeZoom;
		this.relZoomY = relativeZoom;
	}
	
	/**
	 * Creates a new Graphics2DZoom object with a relative zoom of
	 * the passed parameters (relativeZoomX, relativeZoomY).
	 * @param relativeZoomX - the relative zoom for x of this
	 * @param relativeZoomY - the relative zoom for y of this
	 */
	public Graphics2DZoom(double relativeZoomX, double relativeZoomY) {
		this.relZoomX = relativeZoomX;
		this.relZoomY = relativeZoomY;
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
		
		// Makes new zoom relative to absolute zoom scale
		double totZoomX = zoomX * relZoomX;
		double totZoomY = zoomY * relZoomY;

		// Shifts and zooms to the new location
		g.setTransform(getTransform(x, y, zoomX, zoomY, width, height));
	}

	/**
	 * Zooms in the passed Graphics2D object to the given scale (zoom),
	 * for both x and y, and passed location (x, y), 
	 * zooming to the the current relative zoom factor.
	 * (x,y) will be zoomed to the location of the middle of the window
	 * with the passed width by height.
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
	 * Returns the AffineTransform given by the given scale (zoomX, zoomY),
	 * for both x and y, and passed location (x, y), 
	 * zooming to the the current relative zoom factor.
	 * This transformation would zoom (x,y) to the location of the 
	 * middle of the window with the passed width by height.
	 * @param x - x position to zoom to
	 * @param y - y position to zoom to
	 * @param zoomX - x zoom scale, relative to absolute zoom scale
	 * @param zoomY - y zoom scale, relative to absolute zoom scale
	 * @param width - width of the drawing area
	 * @param height - height of the drawing area
	 * @returns the AffineTransform to move (x,y) to the middle of the screen,
	 * 		    with the given scale (zoomX, zoomY)
	 */
	public AffineTransform getTransform(double x, double y,
										double zoomX, double zoomY,
										double width,
										double height) {
		AffineTransform ret = new AffineTransform();
		
		// Shifts and zooms to the new location
		double totZoomX = zoomX * relZoomX;
		double totZoomY = zoomY * relZoomY;	
		ret.translate(-(x - (width / (2.0 * totZoomX))) * totZoomX,
				-(y - (height / (2.0 * totZoomY))) * totZoomY);
		ret.scale(totZoomX, totZoomY);
		
		// Returns the new affine transform
		return ret;
	}
	
	/**
	 * Returns the AffineTransform given by the given scale (zoom),
	 * for both x and y, and passed location (x, y), 
	 * zooming to the the current relative zoom factor.
	 * This transformation would zoom (x,y) to the location of the 
	 * middle of the window with the passed width by height.
	 * @param g - Graphics2D object to zoom
	 * @param x - x position to zoom to
	 * @param y - y position to zoom to
	 * @param zoom - zoom scale, relative to absolute zoom scale
	 * @param width - width of the drawing area
	 * @param height - height of the drawing area
	 * @returns the AffineTransform to move (x,y) to the middle of the screen,
	 * 		    with the given scale (zoom)
	 */
	public AffineTransform getTransform(double x, double y,
										double zoom,
										double width,
										double height) {
		return getTransform(x, y, zoom, zoom, width, height);
	}

	/**
	 * Returns the current absolute (relative) zoom scale for x.
	 * @returns the double value of the current absolute zoom scale for x
	 */
	public double getAbsZoomX() {
		return relZoomX;
	}
	
	/**
	 * Returns the current absolute (relative) zoom scale for y.
	 * @returns the double value of the current absolute zoom scale for y
	 */
	public double getAbsZoomY() {
		return relZoomX;
	}

	/**
	 * Sets the current absolute (relative) zoom scale for x.
	 * @param newScale - the new value of the current absolute zoom scale for x
	 */
	public void setAbsZoomX(double newScale) {
		this.relZoomX = newScale;
	}
	
	/**
	 * Sets the current absolute (relative) zoom scale for y
	 * @param newScale - the new value of the current absolute zoom scale for y
	 */
	public void setAbsZoomY(double newScale) {
		this.relZoomY = newScale;
	}
}





