# cubecolor

Normal cube readers read only one face at a time. This one reads 3 faces at a time, 
allowing for orientation-independent reading.

Currently, it is only made to work with stickered/tiled cubes with black pieces, on 
a white background. Algorithm will need a complete overhaul to allow for more 
flexibility. A possible workaround is to have the user select the vertices.

First, it gets the outline of the cube (~6 points) to create a mask to isolate the 
cube. Then, the colors are analyzed. Three "onion" layers are extracted from the 
facelet vertices.

Todo:

Get rings to determine positions. Piece closest to CM of each face is center piece. 
Closest corner piece might be determined by facelets closest to CM of all for reasonable 
viewing angles...

Maybe approach differently. Find hexagon using the maximize solidity method?

Doesn't work for video input and for empty input. Add a bit of checking.

Fix 0 vs 180 degree clustering for sideways cube (low priority).

Adjust color ranges based on center color. Make HSV range finder tool.

Manually selected vertices.
