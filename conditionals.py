let = 30

if let >= 30:
    print("primero")
else:
    print("segundo")

if let == 30:
    print("primero")
else:
    print("segundo")

colors = ["black", "red"]

if "blue" in colors:
    print("blue matched")
elif "red" in colors:
    print("red matched")
else:
    print("no matches")

colors.append("blue")

if "blue" in colors and "red" in colors:
    print("both matched")
else:
    print("no matches")

if not("pink" in colors):
    print("YES")
else:
    print("NO")