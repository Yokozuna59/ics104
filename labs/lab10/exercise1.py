from random import randint

GRADES = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]


def main():
    files = open("LetterGrades.txt", "w")

    for _ in range(1000):
        number = randint(0, 8)
        element = GRADES[number]
        files.write(element + "\n")
    files.close()


main()
