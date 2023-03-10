Liste = [8, 24, 48, 2, 16]

def mul(Liste):
    count = 0
    i = 0
    for i in range (len(Liste)):
        if Liste[i] % 3 == 0:
            count = count +1
    print(count)

mul(Liste)
    

