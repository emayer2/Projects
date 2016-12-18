package Graphics2DZoom;

/**
 * <p>ZoomTransition creates a transition of states of zoom that
 * can be applied to a Graphics2D object for smooth transitions from
 * one zoom to another, with a given step size.</p>
 * 
 * <p>This class is non-static.</p>
 * 
 * @author Ethan Mayer
 */
public class ZoomTransition {
	/**
	 * Abstraction Function:
	 *  ZOOM_START represents the initial zoom of the transition,
	 *  where ZOOM_END represents the final zoom of the transition.
	 *  zoomStep is the difference in zoom between two states of the transition.
	 *  currZoom is the current point that the zoom of the transition is in.
	 *  TODO: Update AF as class is written
	 *  
	 * Representation Invariant:
	 *  min(ZOOM_END, ZOOM_START) <= currZoom <= min(ZOOM_END, ZOOM_START).
	 *  STEP != 0.0
	 *  TODO: Update RI as class is written
	 */
	
	private final double ZOOM_START;  // Starting point of the zoom
	private final double ZOOM_END;    // Ending point of the zoom
	private final double STEP;       // Step size for the transition
	private double currZoom;   // Current point in the zoom
	
	/**
	 * Creates a new transition with the given start zoom, end zoom, and zoom step size.
	 * The transition will step in the direction of start->end, meaning step
	 * will only be considered in terms of magnitude.
	 * @param start - start zoom of the transition
	 * @param end - end zoom of the transition
	 * @param step - magnitude of the step size
	 * @throws IllegalArgumentException if step == 0.0
	 */
	public ZoomTransition(double start, double end, double step) throws IllegalArgumentException {
		// Makes sure the step size isn't 0.0
		if (step == 0.0) {
			System.err.println("Step size must be not equal to 0.0.");
			throw new IllegalArgumentException();
		}
		
		this.ZOOM_START = start;
		this.ZOOM_END = end;
		this.STEP = Math.abs(step);
		this.currZoom = start;
		
		checkRep();
	}
	
	/**
	 * Resets the transition back to the start, only when it is finished.
	 * Nothing happens if not finished.
	 * @modifies this
	 * @effects the current state is back to its starting state
	 */
	public void reset() {
		if (isFinished()) {
			currZoom = ZOOM_START;
		}
	}
	
	/**
	 * Returns if the transition is finished or not.
	 * @returns true if finished, false if not
	 */
	public boolean isFinished() {
		return currZoom == ZOOM_END;
	}
	
	/**
	 * Steps the transition by the magnitude of the set step size,
	 * making the current zoom closer in magnitude of difference to the end zoom,
	 * and greater in magnitude of difference to the start zoom.
	 * Nothing happens if the transition is finished.
	 * @modifies this
	 * @effects the current state of the transition to be closer to the end
	 * 			by one step size
	 */
	public void step() {
		// Only step if not finished with transition
		if (!isFinished()) {
			// Steps in the appropriate direction
			if (ZOOM_END < ZOOM_START) {
				currZoom -= STEP;
				if (currZoom <= ZOOM_END) {
					// Finished with transition
					currZoom = ZOOM_END;
				}
			} else {
				currZoom += STEP;
				if (currZoom >= ZOOM_END) {
					// Finished
					currZoom = ZOOM_END;
				}
			}
		}
		
		checkRep();
	}
	
	/**
	 * Returns the current zoom state of the transition.
	 * @returns the double value of the current zoom state	 
	 */
	public double getZoom() {
		return currZoom;
	}
	
	/**
	 * Returns the start state of the transition.
	 * @returns the double value of the start zoom state	 
	 */
	public double getStart() {
		return ZOOM_START;
	}
	
	/**
	 * Returns the end state of the transition.
	 * @returns the double value of the end zoom state	 
	 */
	public double getEnd() {
		return ZOOM_END;
	}
	
	/**
	 * Returns the step size state of the transition.
	 * @returns the double value of the step size state	 
	 */
	public double getStep() {
		return STEP;
	}
	
	/**
	 * Asserts that the representation invariant holds.
	 */
	public void checkRep() {
		assert (STEP != 0) : "Step size is 0.";
		assert (Math.min(ZOOM_END, ZOOM_START) <= currZoom &&
				currZoom <= Math.min(ZOOM_END, ZOOM_START)) : 
					"Current zoom is outside zoom range.";
	}
}





































