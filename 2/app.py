import sys
array = []
invalidValues = []

example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def createArrayFromInput():
    with open("input.txt", "r") as f:
        for line in f:
            values = line.strip().split(",")
            for value in values:
                array.append(value)

def createArrayFromExample(example):
    values = example.strip().split(",")
    for value in values:
        array.append(value)

def main():
    if len(sys.argv) > 1:
        args = sys.argv
        if args[1] == "example":
            createArrayFromExample(example)
    else:
        createArrayFromInput()
    for item in array:
        values = item.split("-")
        firstId = int(values[0])
        lastId = int(values[1])
        print(f"Number sets: {firstId} - {lastId}\n")

        # GRABS THE NEXT STRINGIFIED NUMBER
        for i in range(firstId, (lastId + 1)):
            iString = str(i)
            print(f"Current number: {iString}")

            # SETS THE PATTERN 0 to J
            for j in range(1, len(iString)//2+1):
                pattern = iString[:j]
                print(f"Current pattern: {pattern}")

                #IF IT DIVIDES EVENLY, CHECK SLICE TO THE REST OF THE SLICES THAT MAKE UP THE NUMBER
                if len(iString) % len(pattern) == 0:
                    if pattern * ((len(iString))//j) == iString:
                        print(f"{pattern} is a pattern within {iString}")
                        invalidValues.append(int(iString))
                        break

    print(invalidValues)
    print(sum(invalidValues))

if __name__ == "__main__":
    main()