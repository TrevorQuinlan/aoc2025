import sys

array = []
coordinates = []
newArray = []
def fillArrayFromInput():
    with open("input.txt", "r") as f:
        for line in f:
            values = line.strip().split("\n")
            for value in values:
                array.append(value)

def fillArrayFromExample():
    with open("example.txt", "r") as f:
        for line in f:
            values = line.strip().split("\n")
            for value in values:
                array.append(value)

def checkRolls(array):
    global markedArray
    roll = '@'
    rolls = 0
    firstRow = 0
    start = 0
    end = len(array[0]) - 1
    lastRow = len(array) - 1

    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            print(f"array[{i}][{j}] {array[i][j]}")
            count = 0
            # CHECK FIRST ROW
            if i == firstRow and j != start and j!= end and array[i][j] == roll:
                for m in range(i, i+2):
                    for n in range(j-1, j+2):
                        if array[m][n] == roll:
                            count += 1
                if count < 5:
                    rolls+=1
                    print(f">>> array[{i}][{j}] += 1 to make {rolls}")
                    coordinates.append((i,j))
                    continue
            if i == firstRow and j == start and (array[i][j] == roll):
                rolls+=1
                print(f">>> array[{i}][{j}] += 1 to make {rolls}")
                coordinates.append((i,j))
                continue
            if i == firstRow and j == end and (array[i][j] == roll):
                rolls+=1
                print(f">>> array[{i}][{j}] += 1 to make {rolls}")
                coordinates.append((i,j))
                continue
            # CHECK LAST ROW
            if i == lastRow and j != start and j!= end and array[i][j] == roll:
                for m in range(i-1, i+1):
                    for n in range(j-1, j+2):
                        if array[m][n] == roll:
                            count+=1
                if count < 5:
                    rolls+=1
                    print(f">>> array[{i}][{j}] += 1 to make {rolls}")
                    coordinates.append((i,j))
                    continue
            if i == lastRow and j == start and (array[i][j] == roll):
                rolls+=1
                print(f">>> array[{i}][{j}] += 1 to make {rolls}")
                coordinates.append((i,j))
                continue
            if i == lastRow and j == end and (array[i][j] == roll):
                rolls+=1
                print(f">>> array[{i}][{j}] += 1 to make {rolls}")
                coordinates.append((i,j))
                continue

            # CHECK ALL OTHER ROWS
            if i != firstRow and i != lastRow and array[i][j] == roll:
                if j == start:
                    for x in range(i-1, i+2):
                        for z in range(j, j+2):
                            if array[x][z] == roll:
                                count+=1
                    if count < 5:
                        rolls+=1
                        print(f">>> array[{i}][{j}] += 1 to make {rolls}")
                        coordinates.append((i,j))
                        continue
                elif j == end:
                    for w in range(i-1, i+2):
                        for q in range(j-1, j+1):
                            if array[w][q] == roll:
                                count+=1
                    if count < 5:
                        rolls+=1
                        print(f">>> array[{i}][{j}] += 1 to make {rolls}")
                        coordinates.append((i,j))
                        continue
                else:
                    for o in range(i-1, i+2):
                        for p in range(j-1, j+2):
                            if array[o][p] == roll:
                                count+=1
                    if count < 5:
                        rolls+=1
                        print(f">>> array[{i}][{j}] += 1 to make {rolls}")
                        coordinates.append((i,j))
                        continue

    for x,y in coordinates:
        charString = list(array[x])
        charString[y] = "."
        array[x] = ''.join(charString)
    if rolls != 0:
        return rolls + checkRolls(array)
    else:
        return rolls

def main():
    if len(sys.argv) > 1:
        args = sys.argv
        if args[1] == "example":
            fillArrayFromExample()
    else:
        fillArrayFromInput()

    rolls = checkRolls(array)
    for line in array:
        print(line)

    print(f"Rolls: {rolls}")
if __name__ == "__main__":
    main()