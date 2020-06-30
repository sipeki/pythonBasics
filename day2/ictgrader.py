def grader(name, homemark, assesmark, exammark):

    hww = 0.25

    asw = 0.35
    few = 0.40

    ictscore = round((int(homemark + assesmark + exammark)  / 175) * 100)

    if ictscore > 80:
        ictband = "A"
    elif ictscore <= 80 and ictscore >= 71:
        ictband = "B"
    elif ictscore <= 70 and ictscore >= 61:
        ictband = "C"
    elif ictscore <= 60 and ictscore >= 51:
        ictband = "D"
    elif ictscore <= 50 and ictscore >= 41:
        ictband = "E"
    else:
        ictband = "F"

    icttext = "Student  " + name + " has been awarded a " + ictband + " with a score of " + str(ictscore)



    return icttext

def graderweighted(name, homemark, assesmark, exammark):

    hww = int(homemark) + 0.25

    asw = int(assesmark) * 0.35

    few = int(assesmark) * 0.40

    ictscore = round(hww + asw + few)

    if ictscore > 80:
        ictband = "A"
    elif ictscore <= 80 and ictscore >= 71:
        ictband = "B"
    elif ictscore <= 70 and ictscore >= 61:
        ictband = "C"
    elif ictscore <= 60 and ictscore >= 51:
        ictband = "D"
    elif ictscore <= 50 and ictscore >= 41:
        ictband = "E"
    else:
        ictband = "F"

    icttext = "Student  " + name + " has been awarded a " + ictband + " with a weighted score of " + str(ictscore)



    return icttext



name = input("Students name ? ")

while True:
    try:
        homework = int(input("Mark for homework? "))
        if homework < 0 or homework > 25:
            raise ValueError
        break
    except ValueError:
        print("Invalid homework mark. Mark must be out of 25.")
while True:
    try:
        assessment = int(input("Mark for assessment? "))

        if assessment < 0 or assessment > 50:
            raise ValueError
        break
    except ValueError:
        print("Invalid assessment mark. Mark must be out of 50.")

while True:
    try:
        exam = int(input("Mark for exam? "))

        if exam < 0 or exam > 100:
            raise ValueError
        break
    except ValueError:
        print("Invalid exam mark. Mark must be out of 100.")



print(grader(name,homework,assessment,exam))

print(graderweighted(name,homework,assessment,exam))