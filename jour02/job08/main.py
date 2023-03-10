def my_function(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine, et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "legumes" and saison == "hiver":
        print("carotte, tipinambour, endives")
    elif type == "legumes" and saison == "été":
        print("artichaud, aubergine, navet")
    else:
        print("t'es relou")

my_function("legumes", "été")
my_function("fruits", "été")
my_function("legumes", "primptemps")