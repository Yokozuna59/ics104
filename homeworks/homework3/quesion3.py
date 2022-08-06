def main():
    gradeCounts = {"A": 8, "D": 3, "B": 15, "F": 2, "C": 6}

    # Get keys of gradeCounts
    gradesKeys = list(gradeCounts)

    # Get values of gradeCounts
    gradesValuesInt = list(gradeCounts.values())

    # Convert values to string
    gradesValuesStr = []
    for element in gradesValuesInt:
        gradesValuesStr.append(str(element))

    # Print grade keys
    print("The keys are:")
    print(" ".join(gradesKeys))

    # Print grade values
    print("The values are:")
    print(" ".join(gradesValuesStr))

    # Print the key:value pairs
    print("The key:value pairs:")
    for element in gradesKeys:
        print(element, gradeCounts[element])

    # Print the key:value pairs in key order
    print("The key:value pairs in key order:")
    for element in sorted(gradesKeys):
        print(element, gradeCounts[element])

    # Print the average
    print("Average of the values:")
    average = sum(gradesValuesInt)/len(gradesValuesInt)
    print(average)

main()