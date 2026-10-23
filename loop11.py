max_grade = 0
failed = 0
passed = 0
summo = 0
count = 0
while True:
    grade = int(input("Enter a grade: "))
    if grade == -1:
        break
    else:
        if grade > max_grade:
            max_grade = grade
        if grade >= 51:
            passed = passed + 1
        else:
            failed = failed + 1
        summo += grade
        count = count + 1
print("Passed: ", passed)
print("Failed: ", failed)
print("Highest grade: ", max_grade)
print("Average grade: ", summo / count)



