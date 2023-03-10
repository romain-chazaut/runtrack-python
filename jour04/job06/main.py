liste = [1, 2, 3, 4, 5]

# for i in range(len(liste)):
#     if i == 0:
#         temp = liste[i]
#         liste[i] = liste[-1]
#         liste[-1] = temp
#         break

# print(liste)

def swap(arr):
    arr[-1],arr[-2]=arr[-2],arr[-1]
    return arr

print(swap(liste))