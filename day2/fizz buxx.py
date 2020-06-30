
i = 1

for i in range(20):

    answer = i
    rFizz = i % 3
    rBuzz = i % 5

    if rFizz == 0:
        answer = "Fizz"

    if rBuzz == 0:
        if str(answer) != "Fizz":
            answer = ""
        answer = str(answer) + "Buzz"


    print(answer)



