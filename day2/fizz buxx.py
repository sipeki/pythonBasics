
i = 1

while i < 21:
    rFizz = i % 3
    rBuzz = i % 5

    if rFizz == 0:
        print("Fizz")

    if rBuzz == 0:
        print("Buzz")


    print(i)
    i = i + 1


