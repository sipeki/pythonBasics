mark = int(input("Enter your mark:"))

if mark > 85:
    print("distinction")
elif mark >= 65 and mark <=85:
    print("pass")
else:
    print("Fail")

if mark > 85:
    print("distinction")
else:
    if mark >= 65 and mark <=85:
        print("pass")
    else:
        print("Fail")
