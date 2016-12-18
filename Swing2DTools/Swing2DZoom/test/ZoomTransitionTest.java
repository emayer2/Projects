package Swing2DZoom.test;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;

import org.junit.Before;
import org.junit.Test;

import Swing2DZoom.ZoomTransition;

public class ZoomTransitionTest {
	private final double TOL = 0.00000001;
	
	private double s1, s2, s3, s4, s5;
	private double e1, e2, e3, e4, e5;
	private double d1, d2, d3, d4, d5;
	private ZoomTransition z1, z2, z3, z4, z5;
	
	private double[] s, d, e;
	private ZoomTransition[] z;
	
	
	/**
	 * Makes sure java assertions are enabled.
	 */
	@Before
	public void checkAssertsEnabled() {
		ImplementationTests.checkAssertsEnabled();
	}
	
	@Before
	public void setUp() {
		// Creates some starts
		s1 = 1.0;
		s2 = 7.0;
		s3 = 0.0;
		s4 = 4.5;
		s5 = 6.7;
		
		// Creates some ends
		e1 = 3.0;
		e2 = 1.0;
		e3 = 2.7;
		e4 = 7.2;
		s5 = 6.7;
		
		// Creates some steps
		d1 = 0.5;
		d2 = 1.0;
		d3 = 0.1;
		d4 = 1.5;
		d5 = -6.0;
		
		// Creates some transitions
		z1 = new ZoomTransition(s1, e1, d1);
		z2 = new ZoomTransition(s2, e2, d2);
		z3 = new ZoomTransition(s3, e3, d3);
		z4 = new ZoomTransition(s4, e4, d4);
		z5 = new ZoomTransition(s5, e5, d5);
		
		// Creates arrays of all zoom variables
		double[] sArr = {s1, s2, s3, s4, s5};
		double[] eArr = {e1, e2, e3, e4, e5};
		double[] dArr = {d1, d2, d3, d4, d5};
		ZoomTransition[] zArr = {z1, z2, z3, z4, z5};
		s = sArr;
		d = dArr;
		e = eArr;
		z = zArr;
	}
	
	
	/* Constructor Tests */
	
	@Test
	public void testZeroScale() {
		// Tests if zero can be a start/end zoom
		new ZoomTransition(0.0, 1.0, 0.5);
		new ZoomTransition(0.0, 2.0, 0.5);
		new ZoomTransition(0.0, 3.5, 0.5);
		new ZoomTransition(10.1, 0.0, 0.5);
		new ZoomTransition(6.5, 0.0, 0.5);
		new ZoomTransition(2.1, 0.0, 0.5);
		new ZoomTransition(0.0, 0.0, 0.5);
	}
	
	@Test(expected=IllegalArgumentException.class)
	public void testZeroStep() {
		// Tests if IllegalArgumentException is thrown for-
		// all constructors with step size of 0.0.
		new ZoomTransition(1.0, 2.0, 0.0);
		new ZoomTransition(2.0, 1.0, 0.0);
		new ZoomTransition(2.5, 2.6, 0.0);
		new ZoomTransition(10.1, 5.6, 0.0);
		new ZoomTransition(19512, 12395, 0.0);
		new ZoomTransition(0.0, 0.0, 0.0);
	}
	
	@Test
	public void testNegativeArgs() {
		// Tests if negative zooms work.
		new ZoomTransition(2.1, -1.0, 10.92);
		new ZoomTransition(6.7, -2.0, -0.65);
		new ZoomTransition(-2.0, 3.5, 5.4);
		new ZoomTransition(-10.1, 5.0, -1.5);
		new ZoomTransition(-6.5, -3.0, 0.53);
		new ZoomTransition(-2.1, -0.9, -1.5);
		new ZoomTransition(8.0, 4.0, 0.5);
	}
	
	
	/* Accessor Tests */
	
	@Test
	public void testGetStart() {
		// Checks if getStart() properly returns the start zoom
		for (int j = 0; j < 5; j++) {
			assertEquals(Math.abs(s[j]), z[j].getStart(), TOL);
		}
	}
	
	@Test
	public void testGetEnd() {
		// Checks if getStart() properly returns the end zoom
		for (int j = 0; j < 5; j++) {
			assertEquals(Math.abs(e[j]), z[j].getEnd(), TOL);
		}
	}
	
	@Test
	public void testGetStep() {
		// Checks if getStart() properly returns the step size
		for (int j = 0; j < 5; j++) {
			assertEquals(Math.abs(d[j]), z[j].getStep(), TOL);
		}
	}
	
	@Test
	public void testGetZoom() {
		// Tests if the zoom is original set to the start zoom
		for (int j = 0; j < 5; j++) {
			assertEquals(s[j], z[j].getZoom(), TOL);
		}
	}
	
	
	/* Step Tests */
	
	@Test
	public void testHugeNumberOfSteps() {
		// Tests if a huge number of steps can be made on any transition
		for (int i = 0; i < 100000; i++) {  // Iterates more steps than any 
								 			// transition would take
			for (int j = 0; j < 5; j++) {
				z[j].step();
			}
		}
	}
	
	@Test
	public void testStepUnchangedBounds() {
		// Tests if stepping leaves the bounds/step unchanged
		for (int i = 0; i < 100000; i++) {  // Iterates more steps than any 
			                                // transition would take
			for (int j = 0; j < 5; j++) {
				z[j].step();
				testTrnstEqBounds(new ZoomTransition(s[j], e[j], d[j]), z[j]);
			}
		}
	}
	
	@Test
	public void testStepChangesCurrZoomForward() {
		// Tests if stepping changes the current zoom
		// by the specified zoom amount, in a forward transition
		for (int i = 0; i < Math.round((e1 - s1) / d1); i++) {
			assertEquals(s1 + (d1 * i), z1.getZoom(), TOL);
			z1.step();
		}
	}
	
	@Test
	public void testStepChangesCurrZoomBackward() {
		// Tests if stepping changes the current zoom
		// by the specified zoom amount, in a forward transition
		for (int i = 0; i < Math.round((e2 - s2) / d2); i++) {
			assertEquals(s2 - (d2 * i), z2.getZoom(), TOL);
			z2.step();
		}
	}
	
	@Test
	public void testStepFinishedZooming() {
		// Tests if stepping after the transition is finished
		// leaves the current zoom as the end zoom state.
		
		// Zooms all transitions to their respective ends
		for (int i = 0; i < 5; i++) {
			assertEquals(s[i], z[i].getStart(), TOL);
			for (int j = 0; j < Math.ceil(Math.abs((e[i] - s[i]) / d[i])); j++) {
				z[i].step();
			}
			assertEquals(e[i], z[i].getZoom(), TOL);
		}
		
		for (int i = 0; i < 100000; i++) {  // Iterates a huge number of times
			for (int j = 0; j < 5; j++) {
				z[j].step();
				assertEquals(e[j], z[j].getZoom(), TOL);
			}
		}
	}
	
	
	/* IsFinished Tests */
	
	@Test
	public void testNewNotFinished() {
		// Tests if a new transiton is not finished
		for (int j = 0; j < 5; j++) {
			assertFalse(z[j].isFinished());
		}
	}
	
	@Test
	public void testNotDoneWhileStepping() {
		// Tests if the transition is not done while stepping
		for (int i = 0; i < 5; i++) {
			assertFalse(z[i].isFinished());
			for (int j = 0; j < Math.ceil(Math.abs((e[i] - s[i]) / d[i])); j++) {
				z[i].step();
			}
			assertTrue(z[i].isFinished());
		}
	}
	
	@Test
	public void testDoneStepping() {
		// Tests if the transition is finished after it steps
		// a huge number of times, after it has finished.
		for (int i = 0; i < 5; i++) {
			assertFalse(z[i].isFinished());
			for (int j = 0; j < Math.ceil(Math.abs((e[i] - s[i]) / d[i])); j++) {
				z[i].step();
			}
			assertTrue(z[i].isFinished());
		}
		
		for (int i = 0; i < 100000; i++) {
			for (int j = 0; j < 5; j++) {
				z[j].step();
				assertTrue(z[j].isFinished());
			}
		}
	}
	
	
	/* Reset Tests */
	
	@Test
	public void testNewResetUnchanged() {
		// Tests if a new transition is the same after it is reset.
		for (int i = 0; i < 5; i++) {
			z[i].reset();
			testTrnstEq(new ZoomTransition(s[i], e[i], d[i]), z[i]);
		}
	}
	
	@Test
	public void testResetMidTransition() {
		// Tests if a transition cannot be reset during a transition.
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < Math.ceil(Math.abs((e[i] - s[i]) / d[i])); j++) {
				z[i].reset();
				z[i].step();
				assertNotEquals(s[i], z[i].getZoom(), TOL);
				testTrnstEqBounds(new ZoomTransition(s[i], e[i], d[i]), z[i]);
			}
			assertEquals(e[i], z[i].getZoom(), TOL);
		}
	}
	
	@Test
	public void testResetAfterFinished() {
		// Tests if the transition is properly reset after it is finished
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < Math.ceil(Math.abs((e[i] - s[i]) / d[i])); j++) {
				z[i].step();
				assertNotEquals(s[i], z[i].getZoom(), TOL);
				testTrnstEqBounds(new ZoomTransition(s[i], e[i], d[i]), z[i]);
			}
			assertTrue(z[i].isFinished());
			z[i].reset();
			testTrnstEq(new ZoomTransition(s[i], e[i], d[i]), z[i]);
		}
	}
	
	
	/* Private Helpers */
	
	/**
	 * Asserts that the passed transitions have equal start, stop, and steps.
	 * @param tr1 - first ZoomTransition to compare
	 * @param tr2 - second ZoomTransition to compare
	 */
	private void testTrnstEqBounds(ZoomTransition tr1, ZoomTransition tr2) {
		assertEquals(tr1.getStart(), tr2.getStart(), TOL);
		assertEquals(tr1.getEnd(), tr2.getEnd(), TOL);
		assertEquals(tr1.getStep(), tr2.getStep(), TOL);
	}
	
	/**
	 * Asserts that the passed transitions have equal start, stop, step,
	 * and current zoom.
	 * @param tr1 - first ZoomTransition to compare
	 * @param tr2 - second ZoomTransition to compare
	 */
	private void testTrnstEq(ZoomTransition tr1, ZoomTransition tr2) {
		testTrnstEqBounds(tr1, tr2);
		assertEquals(tr1.getZoom(), tr2.getZoom(), TOL);
	}
}






















