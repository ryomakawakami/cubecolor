import os

from cubecolor.reader import reader
from cubecolor.display_cube import displayCube

if __name__ == '__main__':
    imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
    pic1 = os.path.join(imageDir, 'r1.jpg')
    pic2 = os.path.join(imageDir, 'r2.jpg')

    cube = [[['x' for i in range(3)] for j in range(3)] for k in range(6)]

    reader(cube, pic1)
    reader(cube, pic2)

    displayCube(cube)
