# Figures out most likely color for each facelet
# Just the mode for each (smarter way would be the most common config or something)
def filterCube(cube):
    output = [[[None for i in range(3)] for j in range(3)] for k in range(6)]
    for i, face in enumerate(cube):
        for j, row in enumerate(face):
            for k, faceletList in enumerate(row):
                if faceletList == None:
                    output[i][j][k] = 'x'
                    continue
                output[i][j][k] = max(set(faceletList), key=faceletList.count)

    return output
