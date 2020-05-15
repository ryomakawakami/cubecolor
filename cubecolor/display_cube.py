def displayCube(cube):
    cubeText = ["" for i in range(9)]

    for i in range(3):
        cubeText[i] = "      "
        for j in range(3):
            cubeText[i] += cube[0][i][j] + " "

    for i in range(3):
        for j in range(1, 5):
            for k in range(3):
                cubeText[i + 3] += str(cube[j][i][k]) + " "

    for i in range(6, 9):
        cubeText[i] = "      "
        for j in range(3):
            cubeText[i] += cube[5][i - 6][j] + " "

    for text in cubeText:
        print(text)
