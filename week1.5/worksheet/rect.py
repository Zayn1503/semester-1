# Worksheet 1.5: Rectangle Class

class Rectangle:
    """A rectangle with a positive integer width and height."""

    def __init__(self, width, height):
        """Create a rectangle with the given width and height."""
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError
        if width <= 0 or height <= 0:
            raise ValueError

        self.width = width
        self.height = height

    def is_square(self):
        """Return True if the rectangle is a square."""
        return self.width == self.height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)