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
