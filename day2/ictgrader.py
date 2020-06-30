def grader(name, homemark, assesmark, exammark):

    ictscore = int(homemark + assesmark + exammark / 175)
    icttext = "The ICT Score for name " + name + " with a score of " + str(ictscore)



    return icttext


name = input("Students name ? ")
homework = int(input("Mark for homework? "))
assessment = int(input("Mark for assessment? "))
exam = int(input("Mark for exam? "))


print(grader(name,homework,assessment,exam))
