list1 = [[{"1": 0, "2": 9}, 4], "s", 3, (1, 2)]
print(list1)

print(list1[len(list1) - 1])

print(list1[len(list1) - 1][1])

print(list1[len(list1) - 1][0])

print(list1[len(list1) - 2])

print(list1[1])

print(list1[0])

print(list1[0][1])

print(list1[0][0])

print(list1[0][0]["2"])

print(list1[0][0]["1"])

tuplalista = list((1, 2, 3, 4, 5, 6, 7))
tuplalista.append(8)
print(tuplalista)

print(len(list(range(1, 10))))

colors = ["green", "red", "blue"]
print("red" in colors)
colors[1] = "yellow"
print("red" in colors)

colors.extend(["violet", "red"])
print(colors)

colors.insert(-2, "black")
print(colors)

colors.pop()
print(colors)

colors.remove("black")
print(colors)

colors.sort(reverse=True)
print(colors)

colors.clear()
print(colors)