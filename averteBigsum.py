def diagonalDifference(arr):
    primaryDiagonal = 0
    secondaryDiagonal = 0

    for i in range(len(arr)):
        primaryDiagonal += arr[i][i]
        secondaryDiagonal += arr[i][len(arr) - 1 - i]
    
    return abs(primaryDiagonal - secondaryDiagonal)