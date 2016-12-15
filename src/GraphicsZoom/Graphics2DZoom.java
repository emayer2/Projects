// Ethan Mayer
// CSE 331 AA
// DrawPath.java draws a picture of the UW campus,
// and a path between two buildings.

package GraphicsZoom;

import java.awt.Graphics2D;

/**
* The Graphics2DZoom class allows for easy zooming of the Java awt Graphics2D object,
* making for easy/convenient zooming, such as zooming to particular positions
* with a given zoom factor, scaling all zooms by a relative factor, etc.
* This class is non-static.
* 
* <author>Ethan Mayer</author>
*/
public class Graphics2DZoom {
	/**
	 * Abstraction Function:
	 * 	relZoom represents the relative scale to zoom to.
	 *  
	 * Representation Invariant:
	 * 	TODO: Update RI as class is written
	 */

	// Zoom members
	private double relZoom;
	
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
	 * Zooms in the passed Graphics2D object to the given scale,
	 * scaling overall by the current relative zoom factor
	 * @param g - Graphics2D object to zoom
	 * @modifies g
	 * @effects the zoom of g
	 * @throws IllegalArgumentException if g is null
	 */
	public void zoom(Graphics2D g) {
		try {	
			g.scale(relZoom, relZoom);
		} catch (NullPointerException e) {
			// g was null, throw an IllegalArgumentException
			System.err.println("Graphics2D parameter g must be non-null.");
			e.printStackTrace();
			throw new IllegalArgumentException();
		}
	}
	
//	/**
//	 * This private helper method gets the current zoom max scale
//	 * to allow the current path to fit on the screen.
//	 * @returns the double value of the max zoom scale
//	 */
//	private double getMaxZoomScale() {
//		double pathToConsider;
//		if (pathLen == 0.0 && prevPathLen == 0.0) {
//			// No paths have been input, current zoom scale should be unzoomed
//			return currZoomScale;
//		} else if (pathLen == 0.0) {
//			// We are zooming out, check previous pathLen
//			pathToConsider = prevPathLen;
//		} else {
//			// Active current path we are zooming to
//			pathToConsider = pathLen;
//		}
//		
//		// Calculates the zoom to allow the path to fit on the screen
//		int smallDim = Math.min(mapimg.getIconWidth(), mapimg.getIconHeight());
//		int longDim = Math.max(mapimg.getIconWidth(), mapimg.getIconHeight());
//		pathToConsider *= CampusPathsMain.SCALE;
//		if (pathToConsider < smallDim) {
//			return zoom_max;
//		} else if (pathToConsider > longDim) {
//			return zoom_min;
//		} else {
//			return ((zoom_min - zoom_max) *
//							((pathToConsider - (double)smallDim) / longDim)) + zoom_min;
//		}
//	}
	
//	/**
//	 * Private helper than zooms to the current zoom factor.
//	 * @param g2 - Graphics2D2D object to zoom with
//	 * @requires g2 != null
//	 * @effects the amount the GUI will be zoomed by
//	 */
//	private static void zoom(Graphics2D g) {
//		// Calculates the amount to translate by
//		double shiftCoeff;
//		if (currZoomScale == 1.0) {
//			shiftCoeff = 0.0;
//		} else {
//			shiftCoeff = (zoomFactor - (1.0 / currZoomScale)) / (currZoomScale - (1.0 / currZoomScale));
//		}
//		
//		// Amount to zoom by
//		double zoom = currZoomScale * zoomFactor * 1.0/CampusPathsMain.SCALE;
//		
//		// Zooms to the appropriate location
//		if (currPath != null && currPath.size() > 0) {
//			// Zooms toward the current zoom position
//			g2.translate((relX - (zoom - 1) * currZoomX) * shiftCoeff,
//					     (relY - (zoom - 1) * currZoomY) * shiftCoeff);
//			g2.scale(zoom, zoom);
//		} else if (currPath == null) {
//			// Zooms toward the standard unzoomed view
//			g2.translate((relX - (zoom - 1) * currZoomX) * shiftCoeff,
//			             (relY - (zoom - 1) * currZoomY) * shiftCoeff);
//			g2.scale(zoom, zoom);
//		} else {
//			// Path is between the same building, don't zoom
//			g2.scale(1.0/CampusPathsMain.SCALE, 1.0/CampusPathsMain.SCALE);
//		}
//	}
	
//	/**
//	 * Increases the current amount of zoom, up to the current
//	 * max zoom scale amount.
//	 * This method calls repaint if zoom was incremented.
//	 * @modifies this
//	 * @effects the amount the GUI will be zoomed to
//	 * on the next repaint() call
//	 */
//	private void zoomIn() {
//		// Steps the zoom factor
//		if (!isZoomed) {  // Currently zooming
//			if (zoomFactor < currZoomScale) {
//				// Zoom, and repaint the new zoom factor
//				zoomFactor += ZOOM_STEP;
//				repaint();
//			} else {
//				// Fully zoomed
//				isZoomed = true;
//				zoomFactor = currZoomScale;
//			}
//		}
//	}
//	
//	/**
//	 * Decreases the current amount of zoom, up to the current
//	 * min zoom scale amount. This method also signals
//	 * for a rezoom if the user requested it.
//	 * This method calls repaint if zoom was decremented.
//	 * @modifies this
//	 * @effects the amount the GUI will be zoomed to
//	 * on the next repaint() call
//	 */
//	private void zoomOut() {
//		// Un-steps the zoom factor
//		if (isZoomed) {  // Unzooming
//			if (zoomFactor > 1.0 / currZoomScale) {
//				// Unzoom, and paint the new zoom factor
//				zoomFactor -= ZOOM_STEP;
//				repaint();
//			} else {
//				// Fully un-zoomed
//				isZoomed = false;
//				zoomFactor = 1.0 / currZoomScale;
//				currZoomX = 0.0;
//				currZoomY = 0.0;
//				currPath = null;  // No more path to draw
//				
//				// Checks if user wants to display another path,
//				// and prepare for that path zoom
//				if (isReZooming) {
//					// reZoomPath is not currPath 
//					isZoomed = false;
//					updatePath(reZoomPath, this.start, this.end);
//					isReZooming = false;
//					repaint();
//				}
//			}
//		}
//	}
	
}






