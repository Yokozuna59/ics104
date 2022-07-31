def readFileIDs(fileName):
    idsFile = open(fileName, "r")
    ids = []

    for line in idsFile:
        strippedLine = line.rstrip()
        if strippedLine != "":
            lineIds = strippedLine.split(" ")
            ids += lineIds

    idsFile.close()
    return ids


def writeFrequenciesNumber(ids):
    idsFrequencies = open("IDsFrequencies.txt", "w")

    index = 0
    while len(ids) != 0:
        currentId = ids[index]
        numberOfOccunce = ids.count(currentId)
        idsFrequencies.write("%s %d\n" % (currentId, numberOfOccunce))

        for _ in range(numberOfOccunce):
            ids.remove(currentId)

    idsFrequencies.close()


def main():
    ids = readFileIDs("IDs.txt")
    writeFrequenciesNumber(ids)


main()
