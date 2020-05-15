# cubecolor

Normal cube readers read only one face at a time. This one reads 3 faces at a time, 
allowing for orientation-independent reading.

Currently, it is only made to work with stickered/tiled cubes with black pieces, on 
a white background. Algorithm will need a complete overhaul to allow for more 
flexibility. A possible workaround is to have the user select the vertices.

First, it gets the outline of the cube (~6 points) to create a mask to isolate the 
cube. Then, the colors are analyzed.

In order to determine what each facelet seen is, the perpendicular bisector between 
each center piece is drawn. Each facelet can be uniquely positioned by the distance 
from each bisector (since each bisector clusters each face into 3 sets). The colors 
of the centers are used to correctly map the facelets to the data representation.

The cube is represented as a 6x3x3 array. White top for green, red, blue, and orange. 
Blue top for white and green top for yellow.

```
 W      0
OGRB   1234
 Y      5
```

Todo:

Maybe approach differently. Find hexagon using the maximize solidity method?

Doesn't work for video input and for empty input. Add a bit of checking.

Fix 0 vs 180 degree clustering for sideways cube (low priority).

Adjust color ranges based on center color. Make HSV range finder tool.

Manually selected vertices.
