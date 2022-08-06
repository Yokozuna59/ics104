def main():
    gradeCounts = { "A": 8, "D": 3, "B": 15, "F": 2, "C": 6 }
    gradesKeys = list(gradeCounts)
    gradesValuesInt = list(gradeCounts.values())
    gradesValuesStr = []
    for element in gradesValuesInt:
        gradesValuesStr.append(str(element))

    print("The keys are:")
    print(" ".join(gradesKeys))

    print("The values are:")
    print(" ".join(gradesValuesStr))

    print("The key:value pairs:")
    for element in gradesKeys:
        print(element, gradeCounts[element])

    print("The key:value pairs in key order:")
    for element in sorted(gradesKeys):
        print(element, gradeCounts[element])

    print("Average of the values:")
    average = sum(gradesValuesInt)/len(gradesValuesInt)
    print(average)

main()
