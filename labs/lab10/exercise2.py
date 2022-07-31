GRADES = {"A+": 4.0, "A": 3.75, "B+": 3.5, "B": 3.0, "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0,}


def main():
    files = open("LetterGrades.txt", "r")
    gpa = 0
    counter = 0

    for line in files:
        stripedString = line.rstrip()
        gpa += GRADES[stripedString]
        counter += 1
    files.close()
    print("The average GPA of the grades in file `LeLetterGrades.txt` is", gpa / counter)

main()
