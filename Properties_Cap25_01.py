"""
    Python 3: Deep Dive (Part 4 - OOP)
    Chap. 25 Read Only and Computed Properties - Coding

    Create a cache for area. Only when the radius change the area will calculate.

    ** Notes for me **
    - The methods radius and area behaves like variables, this is due by the property.
"""

from math import pi


class Circle:

    def __init__(self, radius):
        self._r = radius
        self._area = None

    @property
    def radius(self):
        return print(self._r)

    @radius.setter
    def radius(self, value):
        self._area = None
        self._r = abs(value)
        return print(f'The radius was changed to: {self._r}')

    @property
    def area(self):
        if self._area is None:
            self._area = pi * (self._r ** 2)
        return print(self._area)



if __name__ == '__main__':
    C1 = Circle(1)
    C1.radius
    C1.area
    C1.radius = 3
    C1.area
