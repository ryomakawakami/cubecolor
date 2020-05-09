# cubecolor

Normal cube readers read only one face at a time. This one reads 3 faces at a time, 
allowing for orientation-independent reading.

Currently, it is only made to work with stickered/tiled cubes with black pieces, on 
a white background. Algorithm will need a complete overhaul to allow for more 
flexibility. A possible workaround is to have the user select the vertices.

Basically, the computer vision part is to get the outline of the cube (6 points). 
Once this is done, some math can be done to calculate the position of each facelet.
