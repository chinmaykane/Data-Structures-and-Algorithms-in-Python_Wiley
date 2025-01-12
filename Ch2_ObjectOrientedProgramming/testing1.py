"""
example for class from pg 78
"""

class Vector:

    def __init__(self, d):          # Create a vector of d dimensions, user has to give that input
        self._coords = [0]*d

    def __len__(self):              # Return length of that "thing" we defined earlier
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords

    