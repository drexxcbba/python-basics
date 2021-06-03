foods = ["apples", "bread", "cheese", "milk", "bananas"]

for it in foods:
    print(it)

i = 0

for it in foods:
    i = i + 1
    if it == "cheese":
        print("Yes!")
        break

print(i)

for it in foods:
    if it == "cheese":
        continue
    print(it)

for i in range(1, 10):
    print(i)

for c in "cad":
    if c == 'd':
        print(c)

count = 0
j = 0
while j <= 10:
    count = count + 1
    j = j + 2

print(count)