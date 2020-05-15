def saveColors(cube, positions, clusters, orientation):
    # White red green
    if orientation == 'wr':
        # White
        i = 0
        for facelet in clusters[0]:
            x = 2 - positions[1][i]
            y = 2 - positions[0][i]
            cube[0][x][y] = facelet[4]
            i += 1

        # Red
        i = 0
        for facelet in clusters[1]:
            x = positions[2][i]
            y = positions[3][i]
            cube[3][x][y] = facelet[4]
            i += 1

        # Green
        i = 0
        for facelet in clusters[2]:
            x = positions[4][i]
            y = 2 - positions[5][i]
            cube[2][x][y] = facelet[4]
            i += 1

##########################

    # White blue red
    if orientation == 'wb':
        # White
        i = 0
        for facelet in clusters[0]:
            x = positions[0][i]
            y = 2 - positions[1][i]
            cube[0][x][y] = facelet[4]
            i += 1

        # Blue
        i = 0
        for facelet in clusters[1]:
            x = positions[2][i]
            y = positions[3][i]
            cube[4][x][y] = facelet[4]
            i += 1

        # Red
        i = 0
        for facelet in clusters[2]:
            x = positions[4][i]
            y = 2 - positions[5][i]
            cube[3][x][y] = facelet[4]
            i += 1

##########################

    # White orange blue
    if orientation == 'wo':
        # White
        i = 0
        for facelet in clusters[0]:
            x = positions[1][i]
            y = positions[0][i]
            cube[0][x][y] = facelet[4]
            i += 1

        # Orange
        i = 0
        for facelet in clusters[1]:
            x = positions[2][i]
            y = positions[3][i]
            cube[1][x][y] = facelet[4]
            i += 1

        # Blue
        i = 0
        for facelet in clusters[2]:
            x = positions[4][i]
            y = 2 - positions[5][i]
            cube[4][x][y] = facelet[4]
            i += 1

##########################

    # White green orange
    if orientation == 'wg':
        # White
        i = 0
        for facelet in clusters[0]:
            x = 2 - positions[0][i]
            y = positions[1][i]
            cube[0][x][y] = facelet[4]
            i += 1

        # Green
        i = 0
        for facelet in clusters[1]:
            x = positions[2][i]
            y = positions[3][i]
            cube[2][x][y] = facelet[4]
            i += 1

        # Orange
        i = 0
        for facelet in clusters[2]:
            x = positions[4][i]
            y = 2 - positions[5][i]
            cube[1][x][y] = facelet[4]
            i += 1

##########################

    # Yellow red blue
    if orientation == 'yr':
        # Yellow
        i = 0
        for facelet in clusters[0]:
            x = 2 - positions[1][i]
            y = 2 - positions[0][i]
            cube[5][x][y] = facelet[4]
            i += 1

        # Red
        i = 0
        for facelet in clusters[1]:
            x = 2 - positions[2][i]
            y = 2 - positions[3][i]
            cube[3][x][y] = facelet[4]
            i += 1

        # Blue
        i = 0
        for facelet in clusters[2]:
            x = 2 - positions[4][i]
            y = positions[5][i]
            cube[4][x][y] = facelet[4]
            i += 1

##########################

    # Yellow green red
    if orientation == 'yg':
        # Yellow
        i = 0
        for facelet in clusters[0]:
            x = positions[0][i]
            y = 2 - positions[1][i]
            cube[5][x][y] = facelet[4]
            i += 1

        # Green
        i = 0
        for facelet in clusters[1]:
            x = 2 - positions[2][i]
            y = 2 - positions[3][i]
            cube[2][x][y] = facelet[4]
            i += 1

        # Red
        i = 0
        for facelet in clusters[2]:
            x = 2 - positions[4][i]
            y = positions[5][i]
            cube[3][x][y] = facelet[4]
            i += 1

##########################

    # Yellow orange green
    if orientation == 'yo':
        # Yellow
        i = 0
        for facelet in clusters[0]:
            x = positions[1][i]
            y = positions[0][i]
            cube[5][x][y] = facelet[4]
            i += 1

        # Orange
        i = 0
        for facelet in clusters[1]:
            x = 2 - positions[2][i]
            y = 2 - positions[3][i]
            cube[1][x][y] = facelet[4]
            i += 1

        # Green
        i = 0
        for facelet in clusters[2]:
            x = 2 - positions[4][i]
            y = positions[5][i]
            cube[2][x][y] = facelet[4]
            i += 1

##########################

    # Yellow blue orange
    if orientation == 'yb':
        # Yellow
        i = 0
        for facelet in clusters[0]:
            x = 2 - positions[0][i]
            y = positions[1][i]
            cube[5][x][y] = facelet[4]
            i += 1

        # Blue
        i = 0
        for facelet in clusters[1]:
            x = 2 - positions[2][i]
            y = 2 - positions[3][i]
            cube[4][x][y] = facelet[4]
            i += 1

        # Orange
        i = 0
        for facelet in clusters[2]:
            x = 2 - positions[4][i]
            y = positions[5][i]
            cube[1][x][y] = facelet[4]
            i += 1
