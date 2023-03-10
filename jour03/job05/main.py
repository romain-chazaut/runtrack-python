for num in range(2, 1001):
    verif = True
    for test in range(2, num):
        if num % test == 0:
            verif = False
    if verif == True:
        print(num)