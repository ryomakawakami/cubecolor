import os

from cubecolor.reader.reader import reader
from cubecolor.display_cube import displayCube
from cubecolor.filter_cube import filterCube

if __name__ == '__main__':
    imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
    pic1 = os.path.join(imageDir, 's1.jpg')
    pic2 = os.path.join(imageDir, 's2.jpg')
    bad = os.path.join(imageDir, 'bad.png')

    cubeList = [[[None for i in range(3)] for j in range(3)] for k in range(6)]

    reader(cubeList, pic1)
    reader(cubeList, pic2)

    reader(cubeList, bad)

    cube = filterCube(cubeList)

    displayCube(cube)
