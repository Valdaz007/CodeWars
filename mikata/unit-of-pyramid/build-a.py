## Description
# Given a number of triangles, calculate the least number triangles needed to complete a triangular pyramid.

# Example:
# pyramid(0) -> 1 <br>
# pyramid(1) -> 0 <br>
# pyramid(2) -> 2 <br>
# pyramid(5) -> 4
# 
# Note: A single triangle is a pyramid.


def pyramid(tri:int) -> int:
    if tri == 0:
        return 1
    for i in range(1,tri+1):
        if tri == i**2:
            return 0
        elif tri < i**2:
            return i**2 - tri
        

if __name__ == "__main__":
    print(pyramid(-9))
    print(pyramid(0))
    print(pyramid(10))