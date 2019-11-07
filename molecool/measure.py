import numpy as np

def calculate_distance(rA, rB):
    """
    This function calculates the distance between two points given as numpy arrays.
    
    Parameters
    ----------
    rA, rB : np.ndarry
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between two points.

    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([3.0, 0, 0])
    >>> calculate_distance(r1, r2)
    3.0
    """
    
    difference = (rA - rB)
    distance = np.linalg.norm(difference)
    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    ab_difference = rB - rA
    bc_difference = rB - rC
    theta=np.arccos(np.dot(ab_difference, bc_difference)/(np.linalg.norm(ab_difference)*np.linalg.norm(bc_difference)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
