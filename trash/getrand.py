import random

coll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bigfinal = []


def get():
    final = []
    while len(final) != 2:
        rand = random.choice(coll)
        if rand not in final:
            final.append(rand)
    return final


for i in range(0, 10000000):
    for each in get():
        bigfinal.append(each)

countdict = {1: bigfinal.count(1), 2: bigfinal.count(2), 3: bigfinal.count(3), 4: bigfinal.count(4), 5: bigfinal.count(
    5), 6: bigfinal.count(6), 7: bigfinal.count(7), 8: bigfinal.count(8), 9: bigfinal.count(9), 10: bigfinal.count(10)}

print(countdict)

# Sort the dictionary by value
sorted_x = sorted(countdict.items(), key=lambda kv: kv[1], reverse=True)

print(sorted_x)
