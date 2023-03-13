def triangle(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b:
        print("Ce n'est pas un triangle.")
    elif a == b == c:
        print("Le triangle est équilatéral.")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("Le triangle est isocèle et rectangle.")
        else:
            print("Le triangle est isocèle.")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print("Le triangle est rectangle.")
    else:
        print("Le triangle est quelconque.")

triangle(3, 4, 5)
triangle(6, 8, 8)


