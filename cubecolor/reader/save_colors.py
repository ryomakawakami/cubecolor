def saveColors(cube, positions, clusters, orientation):
    # White red green
    if orientation == 'wr':
        # White
        for i, facelet in enumerate(clusters[0]):
            x = 2 - positions[1][i]
            y = 2 - positions[0][i]
            if cube[0][x][y] == None:
                cube[0][x][y] = [facelet[4]]
            else:
                cube[0][x][y].append(facelet[4])

        # Red
        for i, facelet in enumerate(clusters[1]):
            x = positions[2][i]
            y = positions[3][i]
            if cube[3][x][y] == None:
                cube[3][x][y] = [facelet[4]]
            else:
                cube[3][x][y].append(facelet[4])

        # Green
        for i, facelet in enumerate(clusters[2]):
            x = positions[4][i]
            y = 2 - positions[5][i]
            if cube[2][x][y] == None:
                cube[2][x][y] = [facelet[4]]
            else:
                cube[2][x][y].append(facelet[4])

##########################

    # White blue red
    if orientation == 'wb':
        # White
        for i, facelet in enumerate(clusters[0]):
            x = positions[0][i]
            y = 2 - positions[1][i]
            if cube[0][x][y] == None:
                cube[0][x][y] = [facelet[4]]
            else:
                cube[0][x][y].append(facelet[4])

        # Blue
        for i, facelet in enumerate(clusters[1]):
            x = positions[2][i]
            y = positions[3][i]
            if cube[4][x][y] == None:
                cube[4][x][y] = [facelet[4]]
            else:
                cube[4][x][y].append(facelet[4])

        # Red
        for i, facelet in enumerate(clusters[2]):
            x = positions[4][i]
            y = 2 - positions[5][i]
            if cube[3][x][y] == None:
                cube[3][x][y] = [facelet[4]]
            else:
                cube[3][x][y].append(facelet[4])

##########################

    # White orange blue
    if orientation == 'wo':
        # White
        for i, facelet in enumerate(clusters[0]):
            x = positions[1][i]
            y = positions[0][i]
            if cube[0][x][y] == None:
                cube[0][x][y] = [facelet[4]]
            else:
                cube[0][x][y].append(facelet[4])

        # Orange
        for i, facelet in enumerate(clusters[1]):
            x = positions[2][i]
            y = positions[3][i]
            if cube[1][x][y] == None:
                cube[1][x][y] = [facelet[4]]
            else:
                cube[1][x][y].append(facelet[4])

        # Blue
        for i, facelet in enumerate(clusters[2]):
            x = positions[4][i]
            y = 2 - positions[5][i]
            if cube[4][x][y] == None:
                cube[4][x][y] = [facelet[4]]
            else:
                cube[4][x][y].append(facelet[4])

##########################

    # White green orange
    if orientation == 'wg':
        # White
        for i, facelet in enumerate(clusters[0]):
            x = 2 - positions[0][i]
            y = positions[1][i]
            if cube[0][x][y] == None:
                cube[0][x][y] = [facelet[4]]
            else:
                cube[0][x][y].append(facelet[4])

        # Green
        for i, facelet in enumerate(clusters[1]):
            x = positions[2][i]
            y = positions[3][i]
            if cube[2][x][y] == None:
                cube[2][x][y] = [facelet[4]]
            else:
                cube[2][x][y].append(facelet[4])

        # Orange
        for i, facelet in enumerate(clusters[2]):
            x = positions[4][i]
            y = 2 - positions[5][i]
            if cube[1][x][y] == None:
                cube[1][x][y] = [facelet[4]]
            else:
                cube[1][x][y].append(facelet[4])

##########################

    # Yellow red blue
    if orientation == 'yr':
        # Yellow
        for i, facelet in enumerate(clusters[0]):
            x = 2 - positions[1][i]
            y = 2 - positions[0][i]
            if cube[5][x][y] == None:
                cube[5][x][y] = [facelet[4]]
            else:
                cube[5][x][y].append(facelet[4])

        # Red
        for i, facelet in enumerate(clusters[1]):
            x = 2 - positions[2][i]
            y = 2 - positions[3][i]
            if cube[3][x][y] == None:
                cube[3][x][y] = [facelet[4]]
            else:
                cube[3][x][y].append(facelet[4])

        # Blue
        for i, facelet in enumerate(clusters[2]):
            x = 2 - positions[4][i]
            y = positions[5][i]
            if cube[4][x][y] == None:
                cube[4][x][y] = [facelet[4]]
            else:
                cube[4][x][y].append(facelet[4])

##########################

    # Yellow green red
    if orientation == 'yg':
        # Yellow
        for i, facelet in enumerate(clusters[0]):
            x = positions[0][i]
            y = 2 - positions[1][i]
            if cube[5][x][y] == None:
                cube[5][x][y] = [facelet[4]]
            else:
                cube[5][x][y].append(facelet[4])

        # Green
        for i, facelet in enumerate(clusters[1]):
            x = 2 - positions[2][i]
            y = 2 - positions[3][i]
            if cube[2][x][y] == None:
                cube[2][x][y] = [facelet[4]]
            else:
                cube[2][x][y].append(facelet[4])

        # Red
        for i, facelet in enumerate(clusters[2]):
            x = 2 - positions[4][i]
            y = positions[5][i]
            if cube[3][x][y] == None:
                cube[3][x][y] = [facelet[4]]
            else:
                cube[3][x][y].append(facelet[4])

##########################

    # Yellow orange green
    if orientation == 'yo':
        # Yellow
        for i, facelet in enumerate(clusters[0]):
            x = positions[1][i]
            y = positions[0][i]
            if cube[5][x][y] == None:
                cube[5][x][y] = [facelet[4]]
            else:
                cube[5][x][y].append(facelet[4])

        # Orange
        for i, facelet in enumerate(clusters[1]):
            x = 2 - positions[2][i]
            y = 2 - positions[3][i]
            if cube[1][x][y] == None:
                cube[1][x][y] = [facelet[4]]
            else:
                cube[1][x][y].append(facelet[4])

        # Green
        for i, facelet in enumerate(clusters[2]):
            x = 2 - positions[4][i]
            y = positions[5][i]
            if cube[2][x][y] == None:
                cube[2][x][y] = [facelet[4]]
            else:
                cube[2][x][y].append(facelet[4])

##########################

    # Yellow blue orange
    if orientation == 'yb':
        # Yellow
        for i, facelet in enumerate(clusters[0]):
            x = 2 - positions[0][i]
            y = positions[1][i]
            if cube[5][x][y] == None:
                cube[5][x][y] = [facelet[4]]
            else:
                cube[5][x][y].append(facelet[4])

        # Blue
        for i, facelet in enumerate(clusters[1]):
            x = 2 - positions[2][i]
            y = 2 - positions[3][i]
            if cube[4][x][y] == None:
                cube[4][x][y] = [facelet[4]]
            else:
                cube[4][x][y].append(facelet[4])

        # Orange
        for i, facelet in enumerate(clusters[2]):
            x = 2 - positions[4][i]
            y = positions[5][i]
            if cube[1][x][y] == None:
                cube[1][x][y] = [facelet[4]]
            else:
                cube[1][x][y].append(facelet[4])
