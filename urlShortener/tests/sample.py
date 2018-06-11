from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError('The radius cannot be negative')
    if type(r) is not int or not float:
        raise TypeError('The radius must be integer')
    return pi*(r**2)


# Test function
# radii = [2, 0, -3, 2 + 5j, True, "radius"]
